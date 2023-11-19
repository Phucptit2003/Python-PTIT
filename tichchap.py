MOD = 10**9 + 7

def count_subarrays_with_avg(A, M):
    N = len(A)
    total_count = 0

    for length in range(1, N + 1):
        target_sum = M * length
        dp = [0] * (target_sum + 1)
        dp[0] = 1

        for i in range(N):
            for j in range(target_sum, A[i] - 1, -1):
                dp[j] = (dp[j] + dp[j - A[i]]) % MOD

        total_count = (total_count + dp[target_sum]) % MOD

    return total_count

# Đọc số bộ test từ input
T = int(input())

# Thực hiện các test case
for _ in range(T):
    # Đọc thông tin của bộ test
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Tính và in ra kết quả
    result = count_subarrays_with_avg(A, M)
    print(result)
