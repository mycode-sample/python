# 元组推导式

l = [1, 2, 3, 4, 5, 6]

a = (ele ^ 2 for ele in l)

# 将生成内容直接转换为列表
b = list(a)
print(b)
