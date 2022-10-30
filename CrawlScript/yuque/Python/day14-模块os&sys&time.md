
# day14


## 内容安排

- 带参数的装饰器： Flask 框架  +  DJango缓存
- 模块

   - os
   - sys
   - time（三种时间）
   - datetime 和 timezone


## 回顾 & 补充


#### 函数

想要给value 设置默认是空列表

```python
# 不推荐
def func(data,value=[]):
	pass
	
# 推荐
def func(data,value=None):
	if not value:
		value = []
```

**闭包**

```python
# 不是闭包
def func1(name):
	def inner():
		return 123
	return inner

# 是闭包：封装值 + 内层函数需要使用
def func2(name):
	def inner():
		print(name)
		return 123
	return inner
```

**递归**

```
def func():
	print(1)
	func()
func()
# 无限递归，直到内存栈不足
```


#### 模块


## 带参数的装饰器

```python
## 1：执行ret = xxx(index)
@xxx
def index():
	psss
	
@uuu(9)
def index():
	pass
```

**练习题**

```python
## 写一个带参数的装饰器， 实现：参数是多少，被装饰的函数就要执行多少次，把每次的结果添加到列表中，最后打印输出


def x(counter):
    print('x')
    def wrapper(func):
        print('wrapper')
        def inner(*args,**kwargs):
            v = []
            for i in range(counter):
                data = func(*args,**kwargs)
                v.append(data)
            return v
        return inner
    return wrapper

@x(9)
def index():
    return 1
result = index()
print(result)

### Anwser
x
wrapper
[1, 1, 1, 1, 1, 1, 1, 1, 1]
```


## 函数模块


#### sys模块

```
import sys
```


##### 删除文件脚本

运行脚本 + 文件路径

```
## 删除文件的脚本 ##
import sys
import shutil
path = sys.argv[1]   # argv默认返回当前文件的路径，[1] 表示获取要删除的文件
shutil.rmtree(path)
print('删除成功')
```

运行实例：




#### **进度条案例**

**转移字符**

- \r :  表示光标移动到第一位，后面的字符会覆盖之前的字符，常用于表示进度条

```python
### 案例 1：模拟进度条 ###
import os
import time
start = time.time()
for i in range(1,101):
    # print('{}%\r'.format(i),end='')   #-5.008621454238892
    msg = '%s%%\r' %i
    print(msg,end='')
    time.sleep(0.05)
end = time.time()
result = start - end
print(result)


### 案例 2：读取视频文件并保存 #####
file_size = os.stat('third class for  ps.MP4').st_size
read_size = 0       #读取的大小

with open('third class for  ps.MP4',mode='rb') as f1,open('a.mp4',mode='wb') as f2:
    while  read_size < file_size:
        chunk = f1.read(1024)       					# 每次读取1024个字节
        f2.write(chunk)            						 # 写入1024字节
        read_size += len(chunk)    						 # 检测读取长度
        speed = int(read_size / file_size *100)        	 # 获取读取百分比
        print('{}%\r'.format(speed),end='')
    f1.close()
    f2.close()
```


#### os模块


##### **和操作系统相关的函数块**

- os.path.exists(path)			判断文件是否存在
- os.path.dirname(file)          获取上级目录
- os.path.abspath(file)          获取文件的绝对路径
- os.path.join                          路径的拼接
- os.stat.st_size(file)              获取文件的大小
- os.listdir                               查看一个目录下的所有文件【第一层】
- os.walk                                  找到一个目录下所有的文件夹及其文件【所有层】
