import sys
import os
import json
import time
import logging
import logging.handlers
import psycopg2.pool
import clickhouse_connect
import traceback
from datetime import datetime

if getattr(sys, 'frozen', False):
    APPLICATION_PATH = os.path.dirname(sys.executable)
else:
    APPLICATION_PATH = os.path.dirname('.')
jsonConfig = json.load(open(os.path.join(APPLICATION_PATH, "config.json"), encoding='utf-8'))


class Pg2Ck(object):
    def __init__(self):
        self.ck_conn = None
        self.interval = jsonConfig.get("interval", 5)
        self.init_log()

        self.pg_data_host = jsonConfig["PGSQL_DATA"]["HOST"]
        self.pg_data_user = jsonConfig["PGSQL_DATA"]["USER"]
        self.pg_data_pass = jsonConfig["PGSQL_DATA"]["PASSWORD"]
        self.pg_data_database = jsonConfig["PGSQL_DATA"]["DB"]
        self.pg_data_port = jsonConfig["PGSQL_DATA"]["PORT"]

        self.ck_host = jsonConfig["CLICKHOUSE"]["HOST"]
        self.ck_user = jsonConfig["CLICKHOUSE"]["USER"]
        self.ck_pass = jsonConfig["CLICKHOUSE"]["PASSWORD"]
        self.ck_database = jsonConfig["CLICKHOUSE"]["DB"]
        self.ck_port = jsonConfig["CLICKHOUSE"]["PORT"]
        self.ck_table = jsonConfig["CLICKHOUSE"]["TABLE"]

        self.pg_data_pool = self.init_pg_data_conn_pool()

        if self.ck_conn is None:
            self.ck_conn = self.init_ck_conn()

    # 初始化postgres数据库连接池
    def init_pg_data_conn_pool(self):
        pool = psycopg2.pool.ThreadedConnectionPool(
            minconn=2,
            maxconn=5,
            host=self.pg_data_host,
            database=self.pg_data_database,
            user=self.pg_data_user,
            password=self.pg_data_pass
        )
        return pool

    # 初始化clickhuose连接
    def init_ck_conn(self):
        conn = clickhouse_connect.get_client(
            host=self.ck_host,
            port=self.ck_port,
            username=self.ck_user,
            password=self.ck_pass)
        return conn

    # 初始化日志
    def init_log(self):
        if not os.path.exists("./log"):
            os.makedirs("./log")
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')

        filehandler = logging.handlers.TimedRotatingFileHandler("./log/run.log", when='d', interval=1,
                                                                backupCount=2)  # 每 1(interval) 天(when) 重写1个文件,保留7(backupCount) 个旧文件；when还可以是Y/m/H/M/S
        filehandler.suffix = "%Y-%m-%d.log"  # 设置历史文件 后缀
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        self.logger = logger

    # 获取一个clickhouse连接
    def get_ck_conn(self):
        if self.ck_conn is None:
            self.ck_conn = self.init_ck_conn()
        return self.ck_conn

    # 获取postgres连接
    def get_pg_data_conn_pool(self):
        conn = self.pg_data_pool.getconn()
        return conn

    # 入口程序
    def main(self):
        while True:
            data = []
            current_time = datetime.now()
            current_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            try:
                conn = self.get_pg_data_conn_pool()
                with conn.cursor() as cursor:
                    orders = jsonConfig['ORDERS']
                    for order_id in orders:
                        sql = f"select ts, order_id, name, price from t_order where ts='{current_str}' and order_id='{order_id}'"
                        self.logger.info("exec sql: %s", sql)
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        for row in rows:
                            ts, order_id, name, price = row
                            if len(value) != 0:
                                data.append([ts, order_id, name, price])
                self.pg_data_pool.putconn(conn)
            except:
                etype, value, tb = sys.exc_info()
                error_info_str = ''.join(traceback.format_exception(etype, value, tb))
                self.logger.error("get point data error: %s", error_info_str)

            self.logger.info(f"data: {data}")

            try:
                ck_conn = self.get_ck_conn()
                if len(data) > 0:
                    ck_conn.insert(f"{self.ck_database}.{self.ck_table}", data, column_names=['ts', 'order_id', 'name', 'price'])
                else:
                    self.logger.info("get pg data is empty")
            except:
                etype, value, tb = sys.exc_info()
                error_info_str = ''.join(traceback.format_exception(etype, value, tb))
                self.logger.error("insert data to clickhouse error: %s", error_info_str)
                self.ck_conn = None

            self.logger.info("pg data to clickhouse over", current_str)
            time.sleep(self.interval)

if __name__ == '__main__':
    pc = Pg2Ck()
    pc.main()
