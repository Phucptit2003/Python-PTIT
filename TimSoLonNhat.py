test=int(input())
for _ in range(test):
    s=str(input())
    maxx=0
    sum=0
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            sum=sum*10+int(s[i])
            if i==len(s)-1:
                maxx=max(sum,maxx)
        else:
            maxx=max(sum,maxx)
            sum=0
    print(maxx)
            