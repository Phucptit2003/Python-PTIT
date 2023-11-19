def check(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return n>1

n=int(input())
a=[int(i) for i in input().split()]
tmp=[]
for i in a:
    if check(i):
        tmp.append(i)
tmp.sort()
j=0
for i in a:
    if check(i):
        print(tmp[j],end=" ")
        j+=1
    else:
        print(i,end=" ")