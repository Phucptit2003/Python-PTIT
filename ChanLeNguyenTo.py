def check(s):
    sum=0
    for i in range(len(s)):
        if i%2==0 and int(s[i])%2!=0:
            return False
        elif i%2==1 and int(s[i])%2!=1:
            return False
        sum+=int(s[i])
    
    for i in range(2,int(sum**0.5)+1):
        if sum%i==0:
            return False
    return sum>1
    

test=int(input())
for _ in range(test):
    s=str(input())
    if check(s):
        print("YES")
    else:
        print("NO")