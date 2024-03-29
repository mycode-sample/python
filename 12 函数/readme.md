# 定义函数以及调用函数

定义一个函数需要遵循以下规则：
- 函数定义以`def`开头，后面是函数名及参数。参数放在圆括号中。
- 函数第一行语句可以使用字符串，作为文档说明。
- 函数内容以冒号`:`开始。
- 函数可以有返回值。如果没有返回值，则返回值为`None`。

定义函数的语法如下：
```python
def 函数名 ( 参数 ):
  函数体
```

定义函数后，就可以通过函数名及参数来调用函数：
```python
def func():
  print("hello")

func()
```

如果函数参数是一个对象，那么这个对象是有类型的。如果只是一个变量，则没有类型，也就意味着自动推断参数类型，比如示例代码中的函数`out_string(a, b)`，如果传入`1`和`2`，则结果是`3`，如果传入`'1'`和`'2'`，则结果是`12`。
