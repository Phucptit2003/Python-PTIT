test=int(input())
for _ in range(test):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    minn=b[0]
    k=-1
    check=False
    for i in range(1,len(b)):
        if b[i]<minn:
            k=i
            minn=b[i]
            check=True
    if check==False and b[0]==b[1]:
        print("-1")
    else:
        print(a[0])