
# day15 Json & time


## pip 使用

```
pip 一个内置的第三方包管理工具，可以使用pip安装第三方包
```


## **模块**

- 
内置模块
```
系统自带的模块
```


- 
第三方模块
```
需要安装
```


- 
自定义模块
```
import xxx
xxx.func1()
xxx.func2()
```




### os

- 
os.path.exists(path)			判断文件是否存在

- 
os.path.dirname(file)          获取上级目录

- 
os.path.abspath(file)          获取文件的绝对路径

- 
os.path.join                          路径的拼接，把目录和文件名合成一个路径

- 
os.stat.st_size(file)              获取文件的大小

- 
os.listdir                               查看一个目录下的所有文件【第一层】

- 
os.walk                                  找到一个目录下所有的文件夹及其文件【所有层】

- 
os.mkdir                                创建一个目录（只能在同级下）

- 
os.mkdirs                              创建多级目录（可以多级创建）
```
# 文件创建 #
```


- 
os.rename('filename1','filename2')



### sys

- 
sys.argv

- 
sys是解释器相关的数据

- 
sys.path 默认Python去导入模块时，会按照sys.path 中的路径挨个查找
```
# 可以使用path导入文件夹，但一般不建议这样使用  
sys.path.apped("D:\code\test\lib")
```




##### 案例

```python
import os
import sys
base_dir = os.path.abspath(__file__)	 # __file__ 获取当前文件名 ## 获取当前文件的绝对路径
base_dir2 = os.path.dirname(base_dir)	# 获取当前文件的上级目录的绝对路径	
sys.path.append(base_dir2)				# 当前文件的上级目录的绝对路径添加到系统的path中去，以便from
print(base_dir)
print(base_dir2)

## Conlse ##
E:\PythonCode\oldboys-Pythoncode\Python基础\day16-time&datetime&异常\模块导入.py
E:\PythonCode\oldboys-Pythoncode\Python基础\day16-time&datetime&异常
```


### json

**json**是一个特殊的字符串。【长得像列表/字典/字符串/数字/真假】

**注意:**

	在json中的字符串必须使用**双引号**

**方法**

- 
json.loads()	对数据进行解码，将json对象转化为str对象

- 
json.dumps()    对json数据进行编码，将str转化为json对象

