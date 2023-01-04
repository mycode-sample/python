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
de_ed_s4 = ed_s4.decode("utf-8")
print(de_ed_s4)

# 判断是否以某字符串结束或开始，可以指定起止区间。区间范围是左开右闭
s5 = "我是一个字符串, 最后一位是句号."
print(s5.startswith("我"))
print(s5.startswith("我", 1, 5))
print(s5.endswith("."))
print(s5.endswith(".", 1, 5))

# 把tab转为空格，默认是8个空格，可以通过参数指定
s6 = "c1\tc2\tc3"
print(s6)
print(s6.expandtabs())
print(s6.expandtabs(4))

# 查找字符串find和index，可以指定起止区间。区间范围是左开右闭
# find找不到时返回-1，index会抛出异常
# 可以使用rfind和rindex从右边开始查找字符串
s7 = "张三拿走了李四的手机, 然后把手机卖给村头的王五"
print(s7.find("的"))
print(s7.find("哈哈哈"))
print(s7.find("的", 10, 22))
print(s7.index("的"))
# print(s7.index("的的"))

# 判断字符串中的内容：
# isalnum():至少有一个字符，且为字母或数字时返回True
print("hh哈哈".isalnum())
print("^王无$".isalnum())
# isalpha():至少有一个字符且所有字符都是字母或中文（也就是非特殊字符）返回True
print("哈哈哈123".isalpha())
print("哈哈哈abcABC".isalpha())
print("日文符号の".isalpha())
# isdigit():只包含数字时返回True
print("12345".isdigit())
print("12345abc".isdigit())
# isnumeric():只包含数字字符时返回True
print("12345".isnumeric())
# 只包含十进制数字返回true
print("12345".isdecimal())
print("a12".isdecimal())
print("bcd".isdecimal())
print("\0x12".isdecimal())
# islower():字符串包含至少一个或多个小写字符时返回True
# isupper():字符串包含至少一个或多个大写字符时返回True
print("字母表abc".islower())
print("字母表abcA".islower())
print("字母表ABC".isupper())
print("字母表ABCa".isupper())
# isspace():字符串长度大于零且都是空白字符返回True
print("        ".isspace())
# istitle():字符串是标题化时返回True

# 合并字符串序列并指定分隔符。字符串序列时可以遍历的字符串变量，比如元组或列表
t8 = ("a", "b", "c")
s8 = str.join(",", t8)
print(s8)

# 获取字符串长度
print("长度".__len__())

# 左对齐/右对齐字符串，并使用指定字符填充到指定长度（可选，默认是空格）
s9 = "user name"
print(s9.rjust)
print(s9.rjust(20, "*"))
print(s9.ljust(30, "&"))

# 大小写转换
s10 = "abcDEF"
print(s10.upper())
print(s10.lower())
# 反转大小写
print(s10.swapcase())

# 截取字符串前后的空白
s11 = "   开始结束   "
print(s11.lstrip().center(50, "*"))
print(s11.rstrip().center(50, "*"))
# 可以使用strip()来同时裁剪前后空白
print(s11.strip().center(50, "*"))

# 返回最大/最小字母
s12 = "这是字母表the brown fox JUMP OVER THE"
print(max(s12))
print(min(s12).center(20, "*"))

# 以指定字符分割字符串
s13 = "the brown fox jumps over the lazy dog."
print(s13.split(" "))
# 按行分割字符串
s14 = """
the brown
fox jumps
over the
lazy dog.
"""
print(s14.splitlines())
# 第二个参数控制是否输出换行符
print(s14.splitlines(True))

# 单词首字母大写（标题化）
s15 = "the brown fox jumps over the lazy dog."
print(s15.title())

# 返回指定长度的字符串，新字符串右对齐，左边用0补齐
s16 = "user";
print(s16.zfill(20))
