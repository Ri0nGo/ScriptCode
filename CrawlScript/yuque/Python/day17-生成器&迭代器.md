
# day17 - 生成器 & 迭代器


## 今日内容

- 迭代器
- 生成器
- 装饰器
- 项目结构
- logging模块


## 内容回顾 & 作业

**内容回顾**

1. 
函数（内置/自定义）

   1. 
基本函数的结构
```
def func(a1,a2):
	pass
```


   2. 
参数

   3. 
返回值

   4. 
执行函数

   5. 
函数小高级

   6. 
函数中高级

   7. 
装饰器 & 闭包

   8. 
递归

   9. 
匿名函数

   10. 
内置函数

2. 
模块（内置/第三方/自定义）

   - 内置：time / json / datetime / sys / os / re
   - 第三方

      - 安装：pip install request
      - 安装路径： D:/python38/Lib/site-packages
      - 使用 / 导入
      - 源码安装

         1. 下载文件，解压文件，cmd进入文件
         2. 运行 Python setup.py
   - 自定义
3. 
其他


**作业**

1. 思维导图
2. Python学习笔记
3. 本周作业
4. 复习：从前到后

   1. 笔记
   2. 作业题


## 迭代器（了解）

迭代器：对某一对象

- 可以for循环的对象中的元素进行逐一获取，`__next_`方法
- 可以执行`result.__iter__`方法


## 生成器（函数的变异）

```python
# 函数
def func():
	return 123
func()

# 生成器函数，
def func(arg):
	arg = arg + 1
	yield 1
	yield 2
	yield 100
	
# 函数内部代码不会执行，返回一致生成器对象
v1 = func(2000)

# 生成器是可以被for 循环，一旦开始循环，函数内部代码就会被执行
for item in v1:
    print(item)
```

- yeild from
- 生成器推导式
