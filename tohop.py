mod = 10**9 + 7
dp = [[0] * 1005 for _ in range(1005)]

n, k = map(int, input().split())
for i in range(1000):
    for j in range(i + 1):
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        dp[i][j] %= mod

print(dp[n][k])
