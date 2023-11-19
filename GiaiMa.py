test=int(input())
for _ in range(test):
    s=str(input())
    tmp=[]
    for i in range(len(s)):
        if s[i]>='0' and s[i] <='9':
            t=int(s[i])
            c=tmp.pop()
            while t>0:              
                tmp.append(c)
                t-=1
        else:
            tmp.append(s[i])
    for i in range(len(tmp)):
        if i!=len(tmp)-1:
            print(tmp[i],end="")
        else:
            print(tmp[i])
    

    