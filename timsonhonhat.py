test=int(input())
for _ in range(test):
    s=str(input())
    minn=10**18
    sum=0
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            sum=sum*10+int(s[i])
            if i==len(s)-1:
                minn=min(sum,minn)
        else:
            if sum>0:
                minn=min(sum,minn)
                sum=0
    print(minn)
            