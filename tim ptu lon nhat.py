n=int(input())
a=input()
b=a.split()
b=[int(a) for a in b]
maxx=b[0]
j=1
for i in range(1,n):
    if b[j]>maxx:
        maxx=b[j]
    j+=1
print(maxx)