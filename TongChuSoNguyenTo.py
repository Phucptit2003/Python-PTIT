prime= [0]*4502

def Prime():
    prime[0]=prime[1]=1
    for i in range(2,int(4500**0.5)+1) :
        if prime[i]==0:
            for j in range(i*i,4500,i) :
                prime[j]=1


test=int(input())
Prime()
for _ in range(test):
    Tong=sum(int(i) for i in input())
    if prime[Tong]==0:
        print("YES")
    else:
        print("NO")
    