import math

# Hàm tính ước chung lớn nhất của hai số
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Đọc dữ liệu đầu vào
N = int(input())
A = [int(input()) for _ in range(N)]

# Tạo danh sách cặp phòng có ước chung lớn hơn 1
pairs = []
for i in range(N):
    for j in range(i + 1, N):
        if gcd(A[i], A[j]) > 1:
            pairs.append((A[i], A[j]))

# Tính ước chung lớn nhất của từng cặp và lưu vào một danh sách
gcd_list = [gcd(pair[0], pair[1]) for pair in pairs]

# Tìm giá trị lớn nhất trong danh sách ước chung
max_gcd = max(gcd_list)

# In ra kết quả, giới hạn lưu lượng tối đa là 10^9
result = min(max_gcd, 10**9)
print(result)
