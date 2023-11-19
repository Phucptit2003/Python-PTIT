s=str(input())
k=0
tmp=""
for i in range(len(s)-1,-1,-1):
    tmp+=s[i]
    k+=1
    if k==3 and i!=0:
        tmp+=","
        k=0
s1=""
for i in range(len(tmp)-1,-1,-1):
    s1+=tmp[i]
print(s1)
    