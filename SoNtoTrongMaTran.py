N=1000
prime=[0]*(N+1)
def Prime():
    prime[0]=prime[1]=1
    for i in range(2,int(N**0.5)+1):
        if prime[i]==0:
            for j in range(i*i,N+1,i):
                prime[j]=1

Prime()
n,m=map(int,input().split())
maxx=0
tmp=[]
for i in range(n):
   tmp.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(m):
        if prime[tmp[i][j]]==0:
            if tmp[i][j]>maxx:
                maxx=tmp[i][j]
if maxx==0:
    print("NOT FOUND")
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==maxx:
                s="Vi tri ["+str(i)+"]["+str(j)+']'
                print(s)