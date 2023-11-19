MOD = 10**9 + 7

def count_subarrays_with_avg(arr, M):
    N = len(arr)
    dp_count = [0] * (M * N + 1)
    dp_sum = [0] * (M * N + 1)

    dp_count[0] = 1
    dp_sum[0] = 1

    for num in arr:
        for s in range(M * N, num - 1, -1):
            if dp_sum[s - num] > 0:
                dp_sum[s] = (dp_sum[s] + dp_sum[s - num]) % MOD
                dp_count[s] = (dp_count[s] + dp_count[s - num]) % MOD

    result = 0
    for i in range(1, N + 1):
        result = (result + dp_count[i * M]) % MOD

    return result

# Đọc số bộ test
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    result = count_subarrays_with_avg(A, M)
    print(result)
