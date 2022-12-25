# 数据类型

# python中的数据类型
"""
Number: 数字，不可变
String: 字符串，不可变
List: 列表
Tuple: 元组，不可变
Set: 集合
Dictionary: 字典
"""

# 可以使用type()方法来判断变量类型
var1 = 1
var2 = "卧槽，我要回家"
var3 = [1, 2, 3]
var4 = (1, 2, 3)
var5 = {'a', 'b', 'c'}
var6 = {
    "user": "zhangsan"
}
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
print(type(var6))

# 还可以用isinstance()来判断类型，和type()的区别是，isinstance()会识别父类型

# 可以使用del关键字来删除引用，删除引用后读取变量会报错
del var6
print(var6)
