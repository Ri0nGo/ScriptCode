# 需要恢复的数据库名称
database=test01
# 数据库用户名
db_user=postgres
# 数据库密码
db_pwd=123456
# 容器id
postgres_container_id=c15a72b63fcc
# 需要恢复的表名
tables_array=("table01" "table02")
 
for tablename in ${tables_array[*]}
do
echo exec -i -e PGPASSWORD=$db_pwd $postgres_container_id  /usr/local/bin/psql -d $database -U $db_user -f $tablename
docker exec -i -e PGPASSWORD=$db_pwd $postgres_container_id  /usr/local/bin/psql -d $database -U $db_user -f $tablename
done