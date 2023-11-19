N=4500
prime=[0]*(N+1)
def Try():
    prime[0]=prime[1]=1
    for i in range(2,int(N**0.5)+1):
        if prime[i]==0:
            for j in range(i*i,N+1,i):
                prime[j]=1


def check(s):
    for i in range(len(s)):
        if prime[i]==1 and prime[int(s[i])]!=1:
            return False
        elif prime[i]==0 and prime[int(s[i])]!=0:
            return False
    return True
    
test=int(input())
Try()
for _ in range(test):
    s=str(input())
    if check(s):
        print("YES")
    else:
        print("NO")