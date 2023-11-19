s=str(input())
t=str(input())
tmp=[]
m=0
for i in range(len(s)):
    if s[i]==t[m]:
        tmp.append(i+1)
        m+=1
    else:
        m=0
        