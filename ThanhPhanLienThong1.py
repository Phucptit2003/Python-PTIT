def DFS(i,vs,graph):
    vs[i]=1
    for j in graph[i]:
        vs[j]=1
        DFS(j,vs,graph)

def find(graph,n,m,t):
    

n,m,t=map(int,input().split())
graph=[]
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
cnt=find(graph,n,m,t)