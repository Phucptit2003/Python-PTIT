def tinh_tong_thetich_max(n, thetich_banh, thetich_noi):
    # Khởi tạo một ma trận DP với kích thước (n+1) x (thetich_noi+1)
    dp = [[0] * (thetich_noi + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, thetich_noi + 1):
            # Nếu thể tích bánh Chưng hiện tại vượt quá thể tích nồi, không chọn
            if thetich_banh[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Chọn bánh Chưng có thể tích i hoặc không chọn
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - thetich_banh[i - 1]] + thetich_banh[i - 1])

    return dp[n][thetich_noi]

n,v=map(int,input().split())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
tong_thetich_max = tinh_tong_thetich_max(n, arr,v)

# In ra kết quả
print( tong_thetich_max)
