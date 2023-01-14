s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4, 5}
s3 = {4, 5, 6, 7}


# 求差
s4 = print(s1.difference(s2))
print(s4)
s1.difference_update(s2)
print(s1)

# 求交
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4, 5}
s3 = {4, 5, 6, 7}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)

# 求补
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4, 5}
s3 = {4, 5, 6, 7}
print(s1.symmetric_difference(s2))
print(s1.symmetric_difference(s3))
s1.symmetric_difference_update(s2)
print(s1)
s1.symmetric_difference_update(s3)
print(s1)

# 求并
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4, 5}
s3 = {4, 5, 6, 7}
print(s1.union(s2))

