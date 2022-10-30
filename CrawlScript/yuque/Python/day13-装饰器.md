
# day13-装饰器


## 1、装饰器格式

```python
def 外出函数(参数)：
	def 内层函数(*args,**kwargs):
		return func()
	return inner
	
@外层函数
def index():
	print(123)
	

## 注意 ##
内层函数添加了参数，为了使调用函数的基础上增加了兼容性，为防止参数报错

## 实例 ##
# --- 装饰器 --- #
from functools import wraps


def warpsFun(flag):
    def loginAuth(func):
        @wraps(func)
        def wrapper(*args, **kw):
            # 对操作的数据进行验证
            # 没有通过验证　
            # print(args)
            if not flag:
                return '未通过验证'
                # 通过验证，执行函数
            res = func(*args, **kw)
            # 可以获得函数名称，输入参数，用以日志保持的原始数据
            # print(func.__name__, res)
            # print('*args', args)
            # print('**kw', args)
            return res

        return wrapper

    return loginAuth


@warpsFun(False)
def login(name, pssswd):
    print("登录程序 login")
    return '登录程序'


@warpsFun(True)
def login1(name, pssswd):
    print("登录程序 login1")
    return '登录程序'


if __name__ == "__main__":
    print('False', login("abc", "123"))
    print('True', login1("abc", "123"))
```


## 2、推导式


#### 2.1 列表推导式

	方便快速生成一个列表

- 
基本格式
```
v1 = [i for i in 'Rion']
# 把RION中的每个字符作为列表中的一个单独的元素添加进来
# v1 = ['r', 'i', 'o', 'n']
```

```
## 新浪面试题
def num():
	return [lambda x:x*i for i in range(4)]
print([m(2) for m in num()])

## Anser
结果是 [6,6,6,6]

## analysis
当for循环结束后，i的值为6，此时return 的结果为:[函数，函数，函数，函数]
当 x = 2 时，i为6，故结果为 [6,6,6,6]
```




#### 2.2 集合推导式

```
d1 = {i for i in 'rion'}
# print(d1)
# d2 = list(d1)
# print(d2)
# print(list(d1))
```


#### 2.3 字典推导式

```
v4 = {'k'+str(i):i for i in range(10)}
print(v4)
```


# 总结

- 
装饰器

   - 格式 ： 双层函数
   - 应用：@外层函数
- 
推导式

- 
模块
```
import time
v = time.time() # 获取当前时间
time.sleep(2)	# 延迟2秒
```


