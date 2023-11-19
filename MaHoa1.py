test=int(input())
for _ in range(test):
    s=input()+'!'
    cnt,c=1,s[0]
    for i in range(1,len(s)):
        if s[i]==c:
            cnt+=1
        else:
            print(str(cnt)+c,end="")
            cnt,c=1,s[i]
    print()