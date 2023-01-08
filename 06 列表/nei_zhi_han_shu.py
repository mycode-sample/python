l1 = [1, 2, 3, 4, 5, 6]
print(len(l1))
print(max(l1), min(l1))
t1 = (1, 2, 3, 4, 5)
print(list(t1))

# 追加
l1.append("张三")
print(l1)
# 计数
print(l1.count("张三"))
# 扩展
l1.extend(t1)
print(l1)
# 查找
print(l1.index(1))
# 插入
l1.insert(2, "有人插队")
print(l1)
# 从尾部删除
l1.pop()
print(l1)
l1.pop(2)
print(l1)
# 移除元素
l1.remove("张三")
print(l1)
# 反向
l1.reverse()
print(l1)
# 排序
l1.sort()
print(l1)
# 复制
l2 = l1.copy()
print(l2)
# 清空
l1.clear()
print(l1)
