
# Jupyter Lab
```shell
docker run -d \
  -p 10001:8888 \
  -e JUPYTER_ENABLE_LAB=yes \
  -v /data/docker/jupyter:/opt/notebooks/ \
  -v /usr/share/zoneinfo/Asia/Shanghai:/etc/localtime \
  -v /etc/timezone:/etc/timezone \
  --restart=always \
  --name jupyterlab captainji/jupyterlab

# 容器内部开发的是 8888 端口
```
**注意：**

1. `**docker logs jupyterlab**`** **查看当前docker 的token信息，访问页面后输入token，并设置密码
2. **docker **默认挂载目录`/opt/notebooks/` 
3. **docker **配置文件 `/root/.jupyter/jupyter_config.`
4. 将所需的py文件复制到 `/data/docker/jupyter/` 目录下，刷新网页即可访问到新的文件

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22315891/1667035958382-592523ce-fa50-4b11-830e-2f631ce65ca1.png#averageHue=%23fcfbfa&clientId=u8d32f7a7-2af3-4&from=paste&height=783&id=ue19d11c1&name=image.png&originHeight=1175&originWidth=2240&originalType=binary&ratio=1&rotation=0&showTitle=false&size=135154&status=done&style=none&taskId=ub362d2e3-46e8-4d6b-9b46-bae6d14ab5a&title=&width=1493.3333333333333)

# RabbitMQ
```shell
docker run -d \
  --hostname rabbitmq_rion \
  --name rabbitmq \
  --restart=always \
  -e RABBITMQ_DEFAULT_USER=rion \
  -e RABBITMQ_DEFAULT_PASS=123456 \
  -p 15672:15672 -p 5672:5672 \
  -v /data/docker/rabbitmq:/var/lib/rabbitmq \
  -v /etc/localtime:/etc/localtime:ro \
  -v /etc/timezone:/etc/timezone:ro \
  rabbitmq:management

  # 参数说明：
    --restart=always 重启策略，生产环境一般使用always
```


# Redis
```
sudo docker run \
-p 6379:6379 \
--name redis \
-v /data/redis/redis.conf:/etc/redis/redis.conf  \
-v /data/redis/data:/data \
-d redis redis-server /etc/redis/redis.conf --appendonly yes

# https://cloud.tencent.com/developer/article/1670205
```
`redis.conf`
```
port 6379
pidfile /data/redis_6379.pid
databases 16
save 60 1000
stop-writes-on-bgsave-error yes
dbfilename dump.rdb
dir /data
requirepass 123456
```
> - port：端口
> - pidfile pid文件
> - databases ： 数据库个数

`参考链接`
> [http://www.redis.cn/download.html](http://www.redis.cn/download.html)
> [https://blog.csdn.net/w15558056319/article/details/121414742](https://blog.csdn.net/w15558056319/article/details/121414742)


# Postgresql（timescaledb）
```
docker run -d \
--name timescaledb02 \
-p 5433:5432 \
-e POSTGRES_PASSWORD=123456 \
-v /etc/localtime:/etc/localtime \
-v /data/timescaledb/data:/var/lib/postgresql/data \
timescale/timescaledb:2.9.1-pg14
```

# MongoDB
```
docker run -d \
  --name mongodb \
  --restart always \
  --privileged \
  -p 27017:27017 \
  -v /etc/localtime:/etc/localtime \
  -v /Users/rion/Data/DockerVolumesData/mongodb/data:/data/db \
  -e MONGO_INITDB_ROOT_USERNAME=root \
  -e MONGO_INITDB_ROOT_PASSWORD=123456 \
  mongo mongod --auth

> https://blog.csdn.net/qq_38983728/article/details/87898956
```
> -d: 后台运行容器；
> --name: 指定容器名；
> -p: 指定服务运行的端口；
> -v: 映射目录或文件；
> --privileged 拥有真正的root权限
> --restart=always Docker服务重启容器也启动
> -e MONGO_INITDB_ROOT_USERNAME=admin 指定用户名
> -e MONGO_INITDB_ROOT_PASSWORD=admin123 指定密码
> mongod --auth ：容器默认启动命令是mongod,我们认证需要修改启动命为mongod --auth开启认证



# Etcd
```
docker run -it --name etcd-server \
-p 2379:2379 -p 2380:2380 \
--env ALLOW_NONE_AUTHENTICATION=yes \
-d bitnami/etcd
```

# MySQL
```
docker run -p 3306:3306 \
--name mysql \
-v /data/mysql/data:/var/lib/mysql \
-v /etc/localtime:/etc/localtime \
-e MYSQL_ROOT_PASSWORD=123456 \
-d mysql
```
