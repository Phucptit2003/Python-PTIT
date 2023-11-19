def check(s):
    stop=False
    sum=0
    tich=1
    for i in range(len(s)):
        if i%2==1:
            sum+=int(s[i])
        else:
            if int(s[i])!=0:
                stop=True
                tich=tich*int(s[i])
    if stop==False:
        tich=0
    print(tich," ",sum)

test=int(input())
for _ in range(test):
    s=str(input())
    check(s)