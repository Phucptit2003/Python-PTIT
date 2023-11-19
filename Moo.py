def Check(m,tmp,k):
    if k==0:
        if m==1:
            return 'm'
        else :
            return 'o'
    if (m-tmp[k-1])<0 or (m-tmp[k-1]-k-3)>0:
        if m-tmp[k-1]<0:
            return Check(m,tmp,k-1)
        else:
            return Check(m-tmp[k-1]-k-3,tmp,k-1)
    else:
        if m-tmp[k-1]==1:
            return 'm'
        else:
            return 'o'

m=int(input())
k=0
tmp=[]
s0=3
tmp.append(s0)
while m>s0:
    k+=1
    s0=2*s0+k+3    
    tmp.append(s0)
print(Check(m,tmp,k))
