
# 闭包

- 
**概念**
<br />闭包，为函数创建一块区域（内部变量供自己使用），为他以后执行提供数据。

- 
**实例代码**
```
name = 'Jack'
def Foo(name):
    def wrapper():
        print(name)
    return wrapper
v = Foo('Captain')
v()
```


- 
**执行原理**


![image-20220425222253712](Z:\Study Note\Typora笔记图库\image-20220425222253712.png)
