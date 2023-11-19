N=10000
prime=[0]*(N+1)
def Try():
    prime[0]=prime[1]=1
    for i in range(2,int(N**0.5)+1):
        if prime[i]==0:
            for j in range(i*i,N+1,i):
                prime[j]=1


def check(s):
    sum=0
    for i in range(len(s)-4,len(s)):
        sum=sum*10+int(s[i])
    if prime[sum]==0:
        return True
    else:
        return False
    
test=int(input())
Try()
for _ in range(test):
    s=str(input())
    if check(s):
        print("YES")
    else:
        print("NO")