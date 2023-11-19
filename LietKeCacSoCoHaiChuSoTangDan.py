s=str(input())
tmp=[]
dd=[0]*101
for i in range(0,len(s),2):
    if i+1<len(s) :
        num=int(s[i])*10+int(s[i+1])
        if dd[num]==0:
            tmp.append(num)
            dd[num]=1
tmp.sort()
print(*tmp)