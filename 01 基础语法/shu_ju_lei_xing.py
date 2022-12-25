# 数据类型
type_number = 1  # 数字类型
type_bool = True # 布尔型
type_float = 12345123415313143213412 # 浮点型
type_complex = 1+4j # 复数

print(type_number)
print(type_bool)
print(type_float)
print(type_complex)

# 字符串
s = "这是一串字符串"
print(s)
s2 = "可以使用斜杠进行\n转义，和c/java/cpp一样"
print(s2)
s3 = r"如果加了r就可以\n忽略转义"
print(s3)
# 字符串可以使用 + 进行拼接
print(s + "," + s2)
print("======")

"""
python中可以直接进行字符串截取，语法是:
变量[start:end:step]
start表示开始下标，end表示结束下标，step表示步长
"""
s = "012345678";
print(s[0:8:2])
# 如果没有end和step就是正常下标
print(s[0] + ", " + s[1])
# 步长使用方法：输出下标2~5之间以2为步长的第一个字符
print(s[2:5:2])
# 字符串截取是左闭右开区间，下面的代码会输出12
print(s[1:3])
