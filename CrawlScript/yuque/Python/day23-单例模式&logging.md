
# day23-单例模式&logging


## 一、单例模式


### 1.1、介绍

	单例模式，无论实例化多少次，都是引用同一个内存地址


### 1.2 实现

- 
**初级版本**
```
# 单例模式Simpleton
# 定义：多个实例化对象共用同一个内存地址；无论实例化多少次都用第一次创建的那个对象
# 

class Simpleton(object):
    _instance = None
    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

s1 = Simpleton()
s2 = Simpleton()
s3 = Simpleton()
print(s1,s2,s3)
# 结果
<__main__.Simpleton object at 0x0000027AEA0922B0> <__main__.Simpleton object at 0x0000027AEA0922B0> <__main__.Simpleton object at 0x0000027AEA0922B0>
```


- 
**应用场景**
```
# 数据库连接操作，每当一个用户来访问网站时，我们都需要从数据库进行数据查询
# 所以我们使用单例模式来保持这个连接不断开，且后面的所有连接对象都是第一个连接对象

# 以文件进行模拟
class FileHelper(object):
    instance = None
    def __init__(self,path):
        self.file_obj = open(file=path,mode='a',encoding='utf-8')

    def __new__(cls,*args,**kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

f1 = FileHelper('ccc.txt')
f2 = FileHelper('ddd.txt')
print(f1.file_obj.write('aaa'),id(f1.file_obj))
print(f2.file_obj.write('ccc'),id(f2.file_obj))

# 结果
    3 2316925959072
    3 2316925959072
    ccc.txt 内容为空
    ddd.txt 内容为aaaccc
```




## 1.3 单例模式--加锁

        在一些场景下，使用了多线程进行处理业务，就因为CPU执行代码时会进行轮流执行，当一个线程执行一定的时间就会暂停，然后执行下一个线程。故容易造成生成的类的ID不一致。

```
from threading import Thread,Lock
import time


class SimpletonLock:
    __instance = None
    lock = Lock()
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(0.1)
                cls.__instance = super(SimpletonLock, cls).__new__(cls)
            return cls.__instance

def simpletonStart():
    s = SimpletonLock()
    print(s)

for i in range(10):
    t = Thread(target=simpletonStart)
    t.start()
```


## 字符串格式化



## logging 模块

- 
基本应用

- 
日志处理的本质  Logger / FileHandler / Formatter

- 
推荐处理日志的方式
```python
import logging

file_handler = logging.FileHandler(filename='x1.log', mode='a', encoding='utf-8',)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[file_handler,],
    level=logging.ERROR
)

logging.error('你好')
```


- 
推荐处理日志方式 + 日志分割
```python
import time
import logging
from logging import handlers
# file_handler = logging.FileHandler(filename='x1.log', mode='a', encoding='utf-8',)
file_handler = handlers.TimedRotatingFileHandler(filename='x3.log', when='s', interval=5, encoding='utf-8')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[file_handler,],
    level=logging.ERROR
)

for i in range(1,100000):
    time.sleep(1)
    logging.error(str(i))
    
# TimedRotatingFileHandler 是用来进行日志切割的，他会自动添加时间
```


- 
保存日志的异常信息
```python
# 在应用日志时，如果想要保留异常的堆栈信息。
import logging
import requests

logging.basicConfig(
    filename='wf.log',
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.ERROR
)

try:
    requests.get('http://www.xxx.com')
except Exception as e:
    msg = str(e) # 调用e.__str__方法
    logging.error(msg,exc_info=True)
```




## 项目结构目录


### 脚本


### 单可执行文件

```
pro1
	-- config		# 存放配置文件
	-- db			# 存放数据库相关文件
		-- user.txt
	-- lib			# 存放公共文件
		-- comment.py
	-- src			# 存放项目特殊文件
		-- order.py
		-- acount.py
		-- run.py
	-- app.py		# 启动文件
```


### 多执行文件

```python
pro1
	-- config		# 存放配置文件
	-- db			# 存放数据库相关文件
		-- user.txt
	-- lib			# 存放公共文件
		-- comment.py
	-- src			# 业务代码文件
		-- order.py
		-- acount.py
		-- run.py
	-- bin			# 启动文件中包含多个
		-- student.py
		-- teacher.py
		-- leader.py
		
# ===============================
 对于上述的多执行文件结构，可执行文件需要导入系统的path路径，这样调用的时候就会方便一些
import os 
import sys
BASE_DIR = os.path.dirname(os.path.dirname(ps.path.abs(__file__)))
sys.path.append(BASE_DIR)
```
