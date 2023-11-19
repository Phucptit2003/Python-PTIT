def check(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=1
    return sum

n=int(input())
if n<0:
    n=-1*n
print(check(n))