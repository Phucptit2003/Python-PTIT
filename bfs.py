from collections import defaultdict,deque

def Bfs(tmp,vs,n,m):
    queue=deque([1])
    vs[1]=1
    while len(queue)>0:
        u=queue.popleft()
        print(u)
        for i in tmp[u]:
            if vs[i]==0:
                queue.append(i)
                vs[i]=1
    

n,m=map(int,input().split())

vs=[0]*(n+1)
tmp=defaultdict(list)
for _ in range(m):
    i,j=map(int,input().split())
    tmp[i].append(j)
    tmp[j].append(i)
Bfs(tmp,vs,n,m)
