a = int(input())
lst = []
for i in range(a):
    x = int(input())
    lst.append(x)

for i in lst:
    print(bin(i).lstrip("0b"))