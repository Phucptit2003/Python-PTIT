test=int(input())
for _ in range(test):
    n=int(input())
    arr=[int(x) for x in input().split()]
    minn=min(arr)
    maxx=max(arr)
    dd=[0]*1002
    for num in arr:
        dd[num]=1
    cnt=0
    for i in range(minn,maxx+1):
        if dd[i]==0:
            cnt+=1
    print(cnt)