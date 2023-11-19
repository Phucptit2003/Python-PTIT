test=int(input())
for _ in range(test):
    s=str(input())
    if s[0]==s[-2] and s[1]==s[-1]:
        print("YES")
    else:
        print("NO")