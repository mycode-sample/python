# while
a = 0
while a < 10:
    a = a+1
    print(a)

print("***")

while a < 10:
    a = a+1
    print(a)
else:
    print("while end")

print("***")

# for
for ele in [1, 2, 3, 4, 5]:
    print(ele)
print("***")

for ele in [1, 2, 3, 4, 5]:
    print(ele)
else:
    print("for end")


print("***")
for e in range(1, 10):
    print(e)
    if e % 2 == 0:
        continue
    elif e == 5:
        break
    else:
        print("current:" + str(e))

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    elif a > 9:
        break
    else:
        print("current:" + str(a))
