# 增删元素
s1 = {1, 2, 3, 4}
print(s1)
s1.add(5)
print(s1)
s1.remove(2)
print(s1)
s1.discard("xyz")
print(s1)
# 由于abc不存在，因此会抛出异常
# s1.remove("abc")
print(s1)
# 给集合添加元素
s1.update({"a", "b", "c"})
print(s1)


# 清空
s1.clear()
print(s1)

# 差运算
s2 = {1, 2, 3, 4}
s3 = {3, 4, 5}
print(s2.difference(s3))

# 两个集合是否含有相同元素
print(s2.isdisjoint(s3))
# s2是否是s3的子集
print(s2.issuperset(s3))

# s4是s3的子集
s4 = {3, 4}
print(s4.issubset(s3))
print(s3.issuperset(s4))
