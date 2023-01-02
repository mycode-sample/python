# 常用函数

# 首字母大写
s1 = "camelCase"
print(s1.capitalize())

# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
s2 = s1
print(s2.center(50, "+"))

# 返回目标字符串出现的次数
s3 = "The fill character must be exactly one character long"
print(s3.count("c"))
# 可以指定查找区间
print(s3.count("c", 0, 20))

# 编码和解码
s4 = "我要编码然后解码"
ed_s4 = s4.encode("utf-8")
print(ed_s4)
de_ed_s4 = ed_s4.decode("utf-8");
print(de_ed_s4)
