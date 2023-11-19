import math

maxn=pow(10,8)
b=[0]*(maxn+1)
b[0]=1
b[1]=1
for i in range (2,int(maxn**0.5)+1):
    if b[i]==0:
        for j in range (i*i,maxn+1,i):
            b[j]=1

n=int(input())
arr=input()
a=arr.split()
a=[int(arr) for arr in a]
s=[0]*(n+1)
for i in a:
    s[i]+=1
for i in a:
    if s[i]>=1 and b[i]==0:
        print(i,end=" ")
        if s[i]>1:
            s[i]=0
