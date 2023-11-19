def check(s,maxx):
    for i in range(0,maxx):
        if s[i]>=s[i+1]:
            return False
    for i in range(maxx,len(s)-1):
        if s[i]<=s[i+1]:
            return False
    return True

test=int(input())
while test>0:
    test-=1
    s=str(input())
    maxx=0
    for i in range(1,len(s)):
        if int(s[i])>int(s[maxx]):
            maxx=i
    if maxx==0 or maxx==len(s)-1:
        print("NO")
    else:
        if check(s,maxx):
            print("YES")
        else :
            print("NO")
    
        
        