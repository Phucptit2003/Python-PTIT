n,m=map(int,input().split())
a=[int(i) for i in input().split()]
dd=[0]*(n+1)
dd[-1]=0
for i in a:
    dd[i]+=1
maxx=max(dd)
stop=False
minn=-1
for i in range(1,m+1):
    if dd[i]>dd[minn] and dd[i]<maxx:
        minn=i
        stop=True
if stop==False:
    print("NONE")
else:
    print(minn)

    