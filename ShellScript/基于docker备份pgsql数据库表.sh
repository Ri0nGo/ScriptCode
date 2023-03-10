# 遇到错误就停止执行后续指令
# set -o errexit
# pgsql容器id
postgres_container_id=c15a72b63fcc
# 数据库备份目录
data_dir=/root/pgdata_backup/
# 数据库密码
db_pwd=123456
# 需要备份的数据库列表
dbs_array=("test" "test02")
# 需要备份的表
tables_array=("table01" "table02" "table03")
# 当前时间
nowtime=$(date +%Y%m%d%H%M%S)
# 数据库备份的绝对路径含时间
data_full_path=${data_dir}${nowtime}
# 压缩包保留前多少天
save_last_days=14

# 创建备份目录
echo ${data_full_path}
if [ ! -d ${data_full_path} ]; then
    mkdir -p ${data_full_path}
fi

# 进入备份目录
cd $data_full_path
for dbname in ${dbs_array[*]}
do
    echo "start backup database name :" ${dbname}
    if [ ! -d ${dbname} ]; then
        mkdir -p ${dbname}
    fi
    cd ${dbname}

    for tablename in ${tables_array[*]}
    do
    echo docker exec -i -e PGPASSWORD=$db_pwd $postgres_container_id  /usr/local/bin/pg_dump -U postgres -d $dbname -t public.$tablename
    docker exec -i -e PGPASSWORD=$db_pwd $postgres_container_id  /usr/local/bin/pg_dump -U postgres -d $dbname -t public.$tablename > $tablename.sql
    done

    cd ../
    echo "end backup database name :" ${dbname}
done

# 压缩文件
cd $data_dir
tar -zcvf $nowtime.tar.gz $nowtime
rm -rf $nowtime

# 删除指定日期之后的文件
find ./ -name "*.tar.gz" -mtime +$save_last_days -exec rm -rfv {} \;

# psql -d db1 -U userA -f /pathA/xxx.sql  恢复指令，针对sql文件
# 参考地址： https://www.cnblogs.com/wuning/p/11778348.html