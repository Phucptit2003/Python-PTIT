n=int(input())
check=False
res=""
tmp=[]
cnt=[]
for j in range(n):
    s=input()
    if check==True:
        cnt.append(s)
        if j==n-1:
            tmp.append(len(cnt))
    if check==False:
        tmp.append(s)
        check=True
    if res==s:
        tmp.append(len(cnt)-1)
        cnt.clear()
        check=False
    
for i in range(0,len(tmp)-1,2):
    print(f"{tmp[i]}: {tmp[i+1]}")    
    
        
    