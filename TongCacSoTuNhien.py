res=[]
tmp=[]

def QL(i,n,tmp):
    if n<0:
        return
    if n==0:
        s="("
        for k in range(len(tmp)):
            if k!=len(tmp)-1:
                s+=str(tmp[k])+" "
            else:
                s+=str(tmp[k])+")"
        res.append(s)
        return

    for j in range(i,0,-1):
        if j<=n:
            tmp.append(j)
            QL(j,n-j,tmp)
            tmp.pop()
            
test=int(input())
for _ in range(test):
    n=int(input())
    tmp.clear()
    res.clear()
    QL(n,n,tmp)
 #   res.sort(reverse=True)
    print(len(res))
    print(*res)
    