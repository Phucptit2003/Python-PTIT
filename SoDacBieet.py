MOD = 10**9+7

def power(n,i):
    result=1
    n=n%MOD
    while i>0:
        if i%2==1:
            result=(result*n)%MOD
        i=i//2
        n=(n*n)%MOD
    return result

def Count(n,k):
    result=0
    i=0
    while k>0:
        if k%2==1:
            result=(result+power(n,i))%MOD
        k=k//2
        i+=1
    return result


test=int(input())
for _ in range(test):
    n,k=map(int,input().split())
    result=Count(n,k)
    print(result)