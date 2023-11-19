n,m=map(int,input().split())
maxx=-1
minn=10001
tmp=[]
for i in range(n):
   tmp.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(m):
        if tmp[i][j]>maxx:
            maxx=tmp[i][j]
        elif tmp[i][j]<minn:
            minn=tmp[i][j]
kc=maxx-minn
check=False
for i in range(n):
    for j in range(m):
        if tmp[i][j]==kc:
            check=True
            break
    if check==True:
        break
            
if check==False:
    print("NOT FOUND")
else:
    print(kc)
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==kc:
                s="Vi tri ["+str(i)+"]["+str(j)+']'
                print(s)