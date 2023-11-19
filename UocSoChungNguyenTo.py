
def Gcd(a,b):
    while b!=0:
        tmp=a%b
        a=b
        b=tmp
    return a

prime=[0]*65
def Prime():
    prime[0]=prime[1]=1
    for i in range(2,int(65**0.5)+1):
        if prime[i]==0:
            for j in range(i*i,65,i):
                prime[j]=1

test=int(input())
Prime()
for _ in range(test):
    a,b=map(int,input().split())
    Uoc=Gcd(a,b)
    sum=0
    while Uoc>0:
        sum+=(Uoc%10)
        Uoc//=10
    if prime[sum] ==0:
        print("YES")
    else:
        print("NO")
    
    