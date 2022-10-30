
# 类成员 & 成员修饰符


## 1、类成员

```
class Foo:
	def __init__(self,name):
		self.name = name
	
	def info(self)
		pass
obj = Foo('rion')
obj2 = Foo('Tom')
```



如果obj对象想取city，则回去Foo类中查找，但是在java中，city取值只能通过Foo查找，对象obj是无法查找的。

- 
类成员

   - 方法
- 
对象成员

   - 实例变量
- 
类变量

   - 
定义：写在类的下一级，即和方法同级

   - 
访问
<br />	类.类变量名称
<br />	对象.类变量名称


**面试题**

```
class Base:
	x = 1
	
obj = Base():
obj.x()
obj.y = 123		# 在对象中创建 y 变量
obj.x = 123		# 在对象中创建 x 变量
Base.x = 666	# 修改Base类中的 x 的值
```

[@staticmethod ](/staticmethod ) 

[@classmethod ](/classmethod ) 


## 成员修饰符

- 公有
- 私有
