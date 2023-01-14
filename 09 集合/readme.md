# 集合

集合是一个无序的不重复序列。

## 创建

可以使用大括号`{}`或者`set()`创建集合。由于`{}`用来创建字典，因此不能使用空的大括号来创建集合
```python
s = {"a", "b", 12345}
```

## 运算

和数学中的集合一样，python中的集合也可以进行并`s1 | s2`、交`s1 & s2`、补`s1 ^ s2`、差`s1 - s2`四种运算。

## 内置方法

1. `add()`和`remove()`：添加和删除集合元素。调用`remove()`时，若删除不存在的元素，会抛出异常。
2. `clear()`：清空。
3. `discard()`: 移除集合中的元素。和`remove()`不同，`discard()`移除不存在元素时不会抛出异常。
4. `update()`: 给集合添加元素。如果该元素存在，则忽略。
5. `pop()`: 随机移除元素并返回被移除的元素。

## 判断集合关系

1. `a.isdisjoint(b)`: 返回集合ab是否有相同元素。
2. `a.issubset(b)`: 集合a是否是集合b的子集。
3. `a.issuperset(b)`: 集合a是否是集合b的父集。

### 集合运算

不带`update`后缀的函数会返回调用结果，不会更新函数调用方。带`update`后缀的函数不会返回内容，而是将调用方更新为不带`update`函数的执行结果。

1. `a.difference(b)`和`a.difference_update(b)`: 求集合的差，即a中有而b中没有的元素。
2. `a.intersection(b)`和`a.intersection_update(b)`: 求集合的交集。
3. `a.symmetric_difference(b)`和`a.symmetric_difference_update(b)`: 求集合的补集，即既不在a中也不在b中的元素。
4. `a.union(b)`: 求并集。
