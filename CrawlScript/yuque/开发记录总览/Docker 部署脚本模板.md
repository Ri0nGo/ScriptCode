
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

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22315891/1667035958382-592523ce-fa50-4b11-830e-2f631ce65ca1.png#clientId=u8d32f7a7-2af3-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=783&id=ue19d11c1&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1175&originWidth=2240&originalType=binary&ratio=1&rotation=0&showTitle=false&size=135154&status=done&style=none&taskId=ub362d2e3-46e8-4d6b-9b46-bae6d14ab5a&title=&width=1493.3333333333333)

# RabbitMQ
```shell
docker run -d \
  --hostname rabbitmq_rion \
  --name rabbitmq \
  --restart=always \
  -e RABBITMQ_DEFAULT_USER=rion -e RABBITMQ_DEFAULT_PASS=Rion_Lucy0928$ \
  -p 15672:15672 -p 5672:5672 \
  -v /data/docker/rabbitmq:/var/lib/rabbitmq \
  -v /etc/localtime:/etc/localtime:ro \
  -v /etc/timezone:/etc/timezone:ro \
  rabbitmq:management

  # 参数说明：
    --restart=always 重启策略，生产环境一般使用always
```
