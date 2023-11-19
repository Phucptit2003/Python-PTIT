def check(i):
    s=str(i)
    if len(s) %2!=0:
        return False
    for i in range(len(s)):
        if int(s[i])%2!=0:
            return False
    l=len(s)
    for i in range(int(l/2)+1):
        if s[i]!=s[l-1-i]:
            return False
    return True
N=10**6+1
tmp=[0]*N
def Find():
    for i in range(22,10**6+1):
        if check(i):
            tmp[i]=1

test=int(input())
Find()
for _ in range(test):
    n=int(input())
    tmp=[]
    for i in range(22,n+1):
        if tmp[i]==1:
            tmp.append(i)
    print(*tmp)