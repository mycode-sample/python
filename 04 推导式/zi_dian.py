# 字典推导式
list = [1, 2, 3, 4, 5]

newDict = {"key:" + str(ele): ele for ele in list}
print(newDict)
