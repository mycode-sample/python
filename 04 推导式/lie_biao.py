# 遍历列表
l = [1, 2, 3, 4, 5]
# 简单表达式
[print(ele) for ele in l]

# 函数表达式


def pr(value):
    print("值:" + str(value))


[pr(ele) for ele in l]


def plus(value):
    print(value)
    return value * 4


# 带返回值的列表表达式
l2 = [plus(ele) for ele in l]
print(l2)

# 带条件的列表表达式
l2 = [plus(ele) for ele in l if ele % 2 == 0]
print(l2)
