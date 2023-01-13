s = {"abc", "def"}
print(s)
s2 = set()

l = [1, 2, 3, 4, 5]
# 参数可以是一个值，也可以是一个可遍历对象
s3 = set(l)
print(s3)

s3 = {"1", "2", "3", "4", "5"}
s4 = {"a", "b", "c", "4", "5", "6", "7"}
print(s3 | s4)
print(s3 & s4)
print(s3 ^ s4)
print(s3 - s4)
