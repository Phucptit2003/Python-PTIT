def check(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return n>1

n=int(input())
print(check(n))