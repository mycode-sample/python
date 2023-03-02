迭代器类似于java中的iterator方法，比如`list.iterator()`。

迭代器有两个基本方法，`iter()`和`next()`。前者用于创建迭代器，后者用于访问迭代器中的下一个元素。需要注意的是，迭代器只能前进，不能后退。

```python
l = [1,2,3]
it = iter(list)
```

迭代器可以使用`for`来遍历：
```python
for ele in iter(list):
  print(ele)
```

# 创建迭代器

创建迭代器需要在类中实现`__next__()`和`__iter__()`方法。
