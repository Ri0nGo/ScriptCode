
## 内容回顾


## 1.Python入门


### 1.1 环境的搭建

- Mac系统上面安装Python环境


### 1.2 变量命名

- 变量 :   小写
- 全局变量： 全字母大写
- 函数


## 2.函数


### 2.1 常用的内置函数

- 
open

- 
id

- 
type

- 
len

- 
range

- 
==  和 is  的区别
<br />可以通过ID进行检查



### 2.2 自定义函数

		函数式编程: 增加代码可读性以及代码重用性。

```
# 函数格式
def show(show,age):
	"""
	函数是干嘛的
	:param name:
	:param age
	:return:
	"""
```

- 
函数做参数

- 
函数做变量

- 
函数做返回值

   - 闭包
   - 装饰器
- 
生成器
```
def func2()
	return [123,12]
def func1():
	print(123)
	yield 1
	yield from func2()	
	yield 2
	
v = func()
# 循环是才会执行yield
# yield from 可以函数在函数之间进行交叉的进行
```




## 3.模块


### 3.1 内置模块

- os
- sys
- json
- datetime
- time
- random


### 3.2 第三方模块

- requests
- xlrd


### 3.3 自定义模块

- 文件
- 文件夹 / 包


### 3.4 使用模块

- 
导入
<br />**注意：**文件和文件夹的命名不能和导入的模块相同，否则就会直接在当前目录中查找

