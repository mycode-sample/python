list = [1, 2, 3, 4]
it = iter(list)
for ele in range(1, 4):
  print(next(it))

for ele in iter(list):
  print(ele)
