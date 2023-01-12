# 字典

## 创建

字典的形式非常像json。字典用花括号定义：
```python
d = {a: 1, b:2}
```

当多个字典进行嵌套时，嵌套结果可以看作json。

除了使用花括号创建字典外，字典还可以使用内置函数`dict()`进行创建：
```python
# 创建空字典
d = dict()
print(len(d))
```

## 修改和删除

可以直接通过访问key来修改或删除字典字典：
```python
d["name"] = "username"
del d["age"]
```

## 字典特性

字典有以下特性：
1. key必须唯一。
2. value可以是任何类型，也可以是空`None`。
3. 如果设置相同key的value，则前一个value会被后一个value覆盖。
4. key必须是不可变的，如果使用可变key，则会抛出异常。

## 内置方法

1. `len(dict d)`：输出长度。
2. `str(dict d)`: 以字符串形式输出字典。输出结果可以看作json对象。
3. `type(variable v)`: 输出参数类型。

## 字典内置方法

1. `clear()`：清空字典。
2. `copy()`：浅复制。
3. `fromkeys(seq, [val])`：创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值。此方法可以通过`dict.fromkeys()`直接调用。
4. `get(key, default=None)`: 返回`key`对应的值。第二个参数用来设置默认值。
5. `key in dict`：这是一个判断语句，若key在字典中，返回`True`，否则返回`False`。
6. `items()`: 以列表形式返回一个视图对象，列表元素是字典k-v组成的元组：`[(k1, v1), (k2, v2), ...]`。
7. `keys()`和`values`: 以例表形式返回所有键或值。
8. `setdefault(key, default=None)`: 设置默认值。如果key不存在，则会添加key并设置默认值为`None`。
9. `dict1.update(dict2)`: 将字典dict2中的键值对更新到dict1中。如果若dict1何dict2有相同键，则覆盖dict1中的键。
10. `popitem()`和`pop(key)`: 删除最后一个键值对或指定键值对并返回被删除的值。
