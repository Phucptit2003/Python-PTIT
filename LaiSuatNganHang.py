test=int(input())
for _ in range(test):
    n,x,m=map(float,input().split())
    sum=n
    cnt=0
    while sum<m:
        a= sum*x/100
        sum+=a
        cnt+=1
    print(cnt)