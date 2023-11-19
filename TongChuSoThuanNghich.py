def check(s):
    if len(s)<2: 
        return False
    sum=0
    for i in range(len(s)):
        sum+=int(s[i])
    tmp=str(sum)  
    if len(tmp)<2:
        return False
    if tmp!=tmp[::-1]:
        return False
    return True
        

test=int(input())
for _ in range(test):
    s=input()
    if check(s):
        print("YES")
    else:
        print("NO")