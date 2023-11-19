def Check(s):
    for i in range(len(s)-2):
        if s[i]!=s[i+2]:
            return False
    return True
        

test=int(input())
for _ in range(test):
    s=str(input())
    a=set()
    for i in s:
        a.add(int(i))
    if len(a)>2:
        print("NO")
    else:
        if Check(s):
            print("YES")
        else:
            print("NO")