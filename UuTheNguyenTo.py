def Prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return n>1

def check(s):
    if Prime(len(s))==False:
        return False
    cntP=0
    cnt=0
    for i in range(len(s)):
        if Prime(int(s[i]))==True:
            cntP+=1
        else:
            cnt+=1
    return cntP>cnt
    
    
test=int(input())
for _ in range(test):
    s=str(input())
    if check(s):
        print("YES")
    else:
        print("NO")