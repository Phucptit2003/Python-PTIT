
def Check(n,m):
    a,b=int(n),int(m)
    while b!=0:
        tmp=a%b
        a=b
        b=tmp
    if a==1: 
        return 'YES'
    else :
        return 'NO'

test=int(input())
for _ in range(test):
    n=input()
    print(Check(n,n[::-1]))
    
    