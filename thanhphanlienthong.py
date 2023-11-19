def DFS(graph,i,vs,v):
    vs[i]=1
    v.append(i)
    for j in graph[i]:
        if vs[j]==0:
            DFS(graph,j,vs,v)

def find(graph,n):
    vs=[0]*(n+1)
    tmp=[]
    for i in range(1,n+1):
        if vs[i]==0:
            v=[]
            DFS(graph,i,vs,v)
            tmp.append(v)
    return tmp
    
n,m=map(int,input().split())
graph=[[]for _ in range(n+1)]

for _ in range (m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=find(graph,n)
print(len(cnt))
for i in cnt:
    print(len(i),end=" ")
    print(*i)