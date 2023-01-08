l1 = ['Google', 'baidu', 1997, 2000]
# 访问第二个元素baidu可以使用l1[2-1]=l1[1]或者l1[2-1-4]=l1[-3]:
print(l1[1], l1[-3])

print(l1[1:3])

l2 = [1, 2, 3, 4, 5]
print(l2)
l2[3] = 12345
print(l2)
del l2[3]
print(l2)
