test=int(input())
lst=[]
for i in range (test):
    n=int(input())
    lst.append(n)

for i in lst:
    print(bin(i).lstrip("0b"))
    