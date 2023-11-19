f='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

test=int(input())
for _ in range(test):
    n,b=map(int,input().split())
    s=""
    while n>0:
        x=n%b
        s=f[x]+s
        n=n//b
    print(s)