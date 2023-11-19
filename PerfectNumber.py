N=10**7
prime=[0]*(N+2)
def Prime():
    prime[0]=prime[1]=1
    for i in range(2,int(N**0.5)+1):
        if prime[i]==0:
            for j in range(i*i,N+1,i):
                prime[j]=1

def check(n):
    if prime[n]==1:
        return False
    m=int(str(str(n)[::-1]))
    if prime[m]==1:
        return False
    s=str(n)
    sum=0
    for i in s:
        if prime[int(i)]==1:
            return False
        sum+=int(i)
    if prime[sum]==1:
        return False
    return True
    
test=int(input())
Prime()
for _ in range(test):
    n=int(input())
    if check(n):
        print("Yes")
    else:
        print("No")