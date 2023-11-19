n=int(input())
a=input()
arr=a.split()
arr=[int(a) for a in arr]
dp=[1]*(n+1)
res=0
for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
    res=max(res,dp[i])
print(res)
