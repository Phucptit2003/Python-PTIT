import math
def Check(sum):
    l=int(sum**0.5)
    for i in range(2,l+1):
        if sum%i==0:
            return False
    return sum>1
        

test=int(input())
for _ in range(test):
    s=str(input())
    sum=0
    for i in range(len(s)-4,len(s)):
        sum=sum*10+int(s[i])
    if Check(sum):
        print("YES")
    else:
        print("NO")