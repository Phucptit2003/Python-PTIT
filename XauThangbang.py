def check(s,tmp):
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(tmp[i])-ord(tmp[i-1])):
            return False
    return True

test=int(input())
for _ in range(test):
    s=str(input())
    tmp=s[::-1]
    if check(s,tmp):
        print("YES")
    else:
        print("NO")
    