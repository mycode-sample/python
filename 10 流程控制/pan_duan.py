# if-else
a = 0

if a == 0:
    print("a = 0")

if a != 0:
    print("a != 0")
elif a == 0:
    print("a = 0")

# match case
a = 2
b = 2
match a == b:
  case True:
    print("a == b")
  case _:
    print("default")
