d = {"name": "张三", "gender": "男", "age": 18}
print(d)
d2 = {"name": "李四", "gender": "女", "age": 38}
print(d2)
d3 = {"name": "王五", "gender": "性别", "age": 18, "father": d, "mother": d2}
print(d3)
print(str(d3))

print(d3["father"])
print(type(d3))

d4 = dict()
print(len(d3))

d2["name"] = "哈哈哈"
print(d2)
del d3["father"]
print(d3)
d3.clear()
print(d3)

d5 = {"user": None}
print(d5)

# 可变key抛出异常
# d6 = {d5: ""}
# print(d6)
