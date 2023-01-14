# 流程控制

学习python除了需要知道基本数据类型和内置函数，还要知道如何做流程控制。和其他语言一样，python也有流程控制，一个是判断，一个是循环。

## 判断

### if-else

语法如下：
```
if 条件1:
    语句1
elif 条件2:
    语句2
else:
    语句3
```

上述判断语句可以进行嵌套：
```
if 条件1:
    if 条件1:
        语句1
    elif 条件2:
        语句2
    else:
        语句3
elif 条件2:
    语句2
else:
    语句3
```

### match-case

语法如下：
```
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
```

和其他语言不同，python使用`case _`标识默认行为，即java和c/cpp中的`default`。

## 循环

循环有两种，一种是使用`for`，一种是使用`while`。两种循环都有不同写法。

### while循环

语法如下：
```
while 条件:
  语句
```

**注意：python中没有`do-while`循环。**

在python中，可以使用`else`来控制while条件不满足时的行为：
```
while 条件:
  语句1
else:
  语句2
```

### for循环

语法如下：
```
for 变量 in 序列:
  语句1
```

和`while`一样，也可以在`for`循环后加`else`:
```
for 变量 in 序列:
  语句1
else:
  语句2
```

### 循环中的continue和break

在循环中，可以使用`continue`跳过当前循环，或者使用`break`跳出循环，通常需要结合判断语句。

```
for 变量 in 序列
  语句1
  if 条件1
    continue
  elif 条件2
    break
  else
    语句3
  语句4
```

```
while 条件
  语句1
  if 条件1
    continue
  elif 条件2
    break
  else
    语句3
  语句4
```

# range函数

如果需要生成数字序列，可以使用`range()`函数:
- `range(a)`: 返回大于等于0小于a的数。
- `range(a,b)`: 返回大于等于a小于b的数。
- `range(a,b,c)`: 返回大于等于a小于b，步长为c的数。

# pass语句

`pass`是一个空语句，没有实际含义，只用来保持语句完整性：
```
for 变量 in 序列
  语句1
  if 条件1
    continue
  elif 条件2
    break
  else
    语句3
  pass
```
