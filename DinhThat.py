res=[]
def DFS(u,v,vs,cnt,tmp):
    if u==v:
        for i in tmp:
            if i!=v:
                cnt[i]+=1
        res.append(tmp)
        return
    for i in graph[u]:
        if vs[i]==0:
            vs[i]=1
            tmp.append(i)
            DFS(i,v,vs,cnt,tmp)
            tmp.pop()
            vs[i]=0
    return
        
        

test=int(input())
for _ in range(test):
    n,m,u,v=map(int,input().split())
    graph=[[]*(n+1) for _ in range(m+1)]
    for i in range(m):
        x,y=map(int,input().split())
        graph[x].append(y)
    vs=[0]*(n+1)
    cnt=[0]*(n+1)
    res.clear()
    tmp=[]
    DFS(u,v,vs,cnt,tmp)
    count=0
    for i in range(n+1):
        if cnt[i]==len(res):
            count+=1
    print(count)
    
        
        