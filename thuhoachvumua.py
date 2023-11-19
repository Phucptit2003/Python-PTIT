n,c=map(int,input().split())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
dp=[[0]*(c+1) for _ in range(n)]
for j in range(c):
    dp[-1][j]=0
for i in range(n):
    for j in range(c+1):
        dp[i][j]=dp[i-1][j]
        if j>=arr[i]:
            dp[i][j]=max(dp[i-1][j-arr[i]]+arr[i],dp[i][j])
print(dp[n-1][c])
        