
# day16 - time & datetime & 异常处理


## 1.模块导入

```python
# 导入模块
import test

# 导入模块中函数
from test import func,show

# 导入模块中的所有函数
from test import *
```


### 1.1 内置模块

- 
os

- 
sys

- 
time

- 
json

   - 
dumps
<br />序列化，保留中文使用ensure_ascii=false

   - 
loads
<br />反序列化

   - 
**注意**

- 
haslib

- 
random

- 
getpass

- 
shutil

- 
copy



## 2.今日内容


### 2.1 json & pickle


#### 2.1.1 json

		优点：所有的语言通用，缺点：只能序列化基本的数据类型


#### 2.1.2 pickle


### 字节类型


### shutil模块

```
# # 删除目录
# shutil.rmtree('FileName')
#
# # 重命名
# shutil.move('oldname','newname')

# 压缩文件
shutil.make_archive('yasuofile','zip','E:\PythonCode\oldboys-Pythoncode\Python基础\lib')

# 解压文件  extract_dir = 制定解压目录，若没有该目录会自动生成一个目录，可以多级创建
shutil.unpack_archive('yasuofile.zip',extract_dir='E:\PythonCode\oldboys-Pythoncode\Python基础\lib',format='zip')
```


### time & datetime

	UTC/GMT  :  世界时间

	本地时间: 本地时区时间


#### time模块

	time.time()     时间戳:  1970-1-1 00:00

	time.sleep(2)    等待秒数

	time.zone  从伦敦到时区之间的秒数，根据电脑系统自动设置的


#### datetime模块

	datetime.now()

	datetime.utcnow()

	datetime.strftime()

	datetime.strptime()

	timedelta		时间变化


