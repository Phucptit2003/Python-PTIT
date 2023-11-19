maxn=pow(10,6)
f=[0]*(maxn+1)
f[0]=1
f[1]=1
for i in range(2,int(maxn**0.5)+1):
    if f[i]==0:
        for j in range(i*i,maxn+1,i):
            f[j]=1

test=int(input())
for _ in range(test):
    l,r=map(int,input().split())
    dem=0
    for i in range(l,r+1):
        if f[i]==0:
            dem+=1
    print(dem)
        