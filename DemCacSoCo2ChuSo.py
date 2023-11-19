s=str(input())
tmp=[]
dd=[0]*101
for i in range(0,len(s),2):
    if i+1<len(s) :
        num=int(s[i])*10+int(s[i+1])
        tmp.append(num)
        dd[num]+=1
for i in tmp:
    if dd[i]>0:
        print(i,dd[i])
        dd[i]=0