test=int(input())
dp=[0]*91
dp[1]=1
dp[2]=2
for i in range(3,91):
    dp[i]=dp[i-1]+dp[i-2]
for _ in range(test):
    n=int(input())
    print(dp[n])
    