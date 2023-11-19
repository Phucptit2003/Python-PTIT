n,m=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
dd=[0]*1001
for i in a:
    dd[i]=1
stop=False
for i in b:
    if dd[i]==0:
        stop=True
        break
if stop==True:
    print("NO")
else:
    print("YES")
        