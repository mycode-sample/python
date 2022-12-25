# 列表

# 列表用方括号定义，不限制每个元素的类型，可以进行嵌套
l = [1, 2, 3]
sl = ["l1", "l2", "l3"]
ll = [l, sl, "user", 123]
print(ll)

# 列表也可以和字符串一样进行截取和重复
nl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nl[1:2])
print(nl[5])
print(nl[0:5:2])
print(nl * 2)

# list有很多内置方法，可以使用intellisense进行学习
