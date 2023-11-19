n,M=map(int,input().split())
tmp=[]
for _ in range(n):
    x,y=map(int,input().split())
    pair=[x,y]
    tmp.append(pair)
f=[[0]*(M+1) for _ in range(n+1)]
for i in range(M):
    f[-1][i]=0
for i in range(n):
    for j in range(M):
        if j>=tmp[i][0]:
            f[i][j]=max(f[i-1][j],f[i-1][j-tmp[i][0]]+tmp[i][1])
        else:
            f[i][j]=f[i-1][j]
res=0
for i in range(len(f)):
    res=max(res,f[i][M-1])
print(res)