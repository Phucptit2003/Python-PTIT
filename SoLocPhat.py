test=int(input())
for _ in range(test):
    s=str(input())
    if s[len(s)-2]=='8' and s[len(s)-1]=='6':
        print("YES")
    else:
        print("NO")