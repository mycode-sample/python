d = {"name": "张三", "gender": "男", "age": 18}
d2 = d.copy()
print(d)

l = ["a", "b", "c", "d"]
d3 = dict.fromkeys(l, ["a", "b"])

print(d3)
d4 = d.copy()

d4.setdefault("age", 20)
d4.setdefault("up", "up")
d4.setdefault("down")

print(d4)
print(d4.get("a"))
print(d4.get("a", "第一个字母"))

print(d.popitem())
print(d.pop("name"))
print(d)

d2["name"] = "李四"
d.update(d2)
print(d)

print("a" in d)
print("name" in d)

v = d.items()
print(v)
v2 = d.keys()
print(v2)
v3 = d.values()
print(v3)

