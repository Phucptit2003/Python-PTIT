def Check(s):
    sum=0
    for i in s:
        sum+=int(i)
    if sum %10==0:
        return True
    else:
        return False
def Check1(s):
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1]))!=2:
            return False
    return True

test=int(input())
for _ in range(test):
    s=str(input())
    if Check(s) and Check1(s):
        print("YES")
    else:
        print("NO")