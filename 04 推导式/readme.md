推导式支持四种数据类型：列表(list)、元组(tuple)、字典(dict)和集合(set)

## 列表推导式
```python
[表达式 for 变量 in 列表]

# 或者

[表达式 for 变量 in 列表 if 条件]
```

表达式可以是拥有返回值的函数，条件可以用来过滤列表中的值。

## 字典推导式

```python
{ key表达式: value表达式 for 值 in 集合 }
{ key表达式: value表达式 for 值 in 集合 if 条件 }
```

key表达式和value表达式分别用来生成字典的key和value。

## 集合推导式

```python
{表达式 for 元素 in 集合}
{表达式 for 元素 in 集合 if 条件}
```

最简单的遍历集合的代码：`{print(ele) for ele in list}`

## 元组推导式（生成器表达式）

元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足条件的元组。

```python
(表达式 for 元素 in 序列)
(表达式 for 元素 in 序列 if 条件)
```

元组推导式和集合推导式一样，只是前者用小括号`()`，后者用中括号`[]`。此外，元组返回的是一个生成
器对象，可以当作无参函数来使用。如果将返回值使用`print()`输出，会看到类似下面的输出：
```
<generator object <genexpr> at 0x00000239C9BDA7A0>
```
