# 字符串
s = "这是一个字符串"
print(s[4:5])
print(s[0])

if ('这' in s):
    print('这')

if ('哈哈' not in s):
    print('哈哈')

print(s * 4)

# %c表示ascii码
print("用户:%s, 年龄:%d, 性别:%c"%("张三", 18, 33))
