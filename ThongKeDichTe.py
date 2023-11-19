m,n = map(int,input().split())
tmp=[]
indx=[-1,-1,-1,0,0,1,1,1]
indy=[-1,0,1,-1,1,-1,0,1]
vs=[[0]*n for _ in range(m)]

cnt=0
for _ in range(m):
    tmp.append([int(i) for i in input().split()])
for i in range(m):
    for j in range(n):
        if tmp[i][j]==-1:
            vs[i][j]=1
            for k in range(8):
                if i+indx[k]>=0 and i+indx[k]<m and j+indy[k]>=0 and j+indy[k]<n:
                    if vs[i+indx[k]][j+indy[k]]==0 and tmp[i+indx[k]][j+indy[k]]!=-1:
                        vs[i+indx[k]][j+indy[k]]=1
                        cnt+=tmp[i+indx[k]][j+indy[k]]
print(cnt)
                
                    
            