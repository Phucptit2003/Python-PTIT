def min_time_to_write(N, X, Y, Z):
    DP = [float('inf')] * (N + 1)
    DP[0] = 0

    for i in range(1, N + 1):
        # Thực hiện thao tác insert
        DP[i] = min(DP[i], DP[i - 1] + X)

        # Thực hiện thao tác delete
        if (i+1 )%2==0:
            DP[i] = min(DP[i], DP[(i+1)//2] +Z + Y)

        # Thực hiện thao tác copy
        if i % 2 == 0:
            DP[i] = min(DP[i], DP[i // 2] + Z)

    return DP[N]

# Đọc số lượng bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    N = int(input())
    X, Y, Z = map(int, input().split())

    result = min_time_to_write(N, X, Y, Z)
    print(result)