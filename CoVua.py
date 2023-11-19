MOD = 10**9 + 7

def count_ways(n, x):
    # Khởi tạo bảng DP với n*2 + 1 phần tử
    DP = [0] * (2 * n + 1)
    DP[2] = 1  # Khởi tạo DP[2]
    DP[3] = 1  # Khởi tạo DP[3]

    # Tính DP[i] cho i từ 4 đến 2n
    for i in range(4, 2 * n + 1):
        DP[i] = (DP[i - 2] * (i - 1) + DP[i - 1] * (i - 2)) % MOD

    # Lấy kết quả từ DP[2n]
    result = DP[2 * n]

    return result

# Đọc input từ người dùng
n, x = map(int, input().split())

# Tính kết quả và in ra
result = count_ways(n, x)
print(result)
