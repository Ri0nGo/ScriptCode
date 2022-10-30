
# 面向对象


## 内容安排

- 面向对象基本用法
- 好处与应用场景
- 面向对象的三大特性


### 面向对象的基本格式

```python
## 基本格式 ## 
class 类名:
    def 方法名(self,name):
        print(name)
        return 123

obj = 类名()
result = obj.方法名('rion')

## 使用案例 ## 
class Account:
    # 方法
    def login(self):
        print('登录')

    def logout(self):
        print('注销')


x = Account()  # 创建了一个Account类的对象
result = x.login()  # 调用对象类中的方法
print(result)
```

-  应用场景<br />遇到很多函数，需要给函数进行区域划分 

```
简单实例
class Person:
    def show(self):
        print(self.name)

p1 = Person()
p1.name = 'RIon'

p2 = Person()
p2.name = 'Jack'

p2.show()
```

**初始化对象**

```
class Persion():
    def __init__(self,name,age,gender):  ## 初始化对象
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        temp = 'I\'m {0},This year is {1}, is a {2}'.format(self.name,self.age,self.gender)
        print(temp)

# 类（） 实例化对象，自动执行此类中的__init__方法。
p1 = Persion('Rion',19,'男')
p1.show()
```


## 总结

	如果写代码时，函数比较多比较乱

1. 可以将函数归类并放到同一个类中。
2. 函数如果有一个反复使用的公共值，则可以放到对象中。


### 案例



## 继承

	父类（基类）

	子类（派生类）

**注意**

- self 到底是谁创建的
- self 到底是哪个类创建的，就从此类开始找，自己没有就找父类


### 多继承

```
class F1:
	psss
	
class F2:
	pass
	
class F3(F1,F2):
	pass
```

---


## 多态（多种形态/多种类型）

```
def func(arg):
	v = argp[-1]
	print(v)
```


### 鸭子模型

```
对于一个
```

---


## 总结


### 面向对象的三大特性

-  封装<br />类是一种封装、将属性和方法封装<br />函数也是一种封装、将具有一定公共的逻辑代码封装到一个函数中，使用的时候直接调用即可，提高代码得扩展性。 
```
class File:
	def read(self):
		pass
	def write(self):
		pass
```
  

-  继承<br />将公共的属性和方法放在父类中，子类只需要关注自己特有的属性和方法，提高代码得扩展性。 
```
class Base():
	pass
class Foo(Base):
	pass
```
 

   - 多继承
   - self到底是谁
   - self出于哪个类创建的，则找方法就从创建他的那个类开始找
-  多肽<br />一个对象在不同的情况下，具有不同的形态，用于强类型语言。是使用在继承和接口实现。<br />**python中有2中不同的说法:**<br />	1、python支持多肽、python是一个弱类型，本身一个变量		名，可以存储任何类型的值，可以理解为多种形态<br />	2、python不支持多肽，多肽本身就是用于强类型的语言的，python是一个弱类型，所以不支持。  

### 格式
```
class 类：
	def __ini__(self,x):
		self.x = x
	def 方法(self,name)
		print(self.x,name)
# 实例化一个类的对象
v1 = 类(666)
v2.方法('Rion')
```
  

### 什么时候用面向对象？

   - **函数（业务功能）比较多**
   - **数据封装（创建字典来存储时，面向对象）**
