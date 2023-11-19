def Find_min(M,arr):
    n=len(arr)
    arr.sort()
    dp=[float('inf')]*(M+1)
    dp[0]=0
    for i in range(n):
        for j in range(arr[i],M+1):
            dp[j]=min(dp[j],dp[j-arr[i]]+1)
    if dp[M]==float('inf'):
        return -1
    return dp[M]

n,M=map(int,input().split())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
result=Find_min(M,arr)
print(result)