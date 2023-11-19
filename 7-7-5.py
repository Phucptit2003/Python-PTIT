def QL(i,c,res,sum):
    if sum>c:
        if sum-arr[i]>res:
            res=sum-arr[i]
        return
    for j in range(i+1,n,1):
        QL(j,c,res,sum+arr[j])
    return res

n,c=map(int,input().split())
string=input()
arr=string.split()
vs=[0]*(n+1)
arr=[int(string) for string in arr]
res=0
print(QL(-1,c,res,0))
