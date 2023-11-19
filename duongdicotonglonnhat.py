
m,n=map(int,input().split())
tmp=[]
for _ in range(m):
    input_string=input()
    arr=input_string.split()
    arr=[int(input_string) for input_string in arr]
    tmp.append(arr)
f=[[0]*(n) for _ in range(m+1)]
for i in range(m):
    for j in range(n):
 
        f[i][j]=max(arr[i-1][j-1],max(arr[i][j-1],arr[i+1][j-1]))+arr[i][j]
res=INT_MIN
for i in range(m):
    res=max(res,f[i][n-1])   
print(res)    