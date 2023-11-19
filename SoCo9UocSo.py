def count_numbers_with_9_divisors(N):
    count = 0
    max_root = int(N ** (1 / 2))  # Lấy căn bậc hai của N
    max_cube_root = int(N ** (1 / 3))  # Lấy căn bậc ba của N

    # Đếm số ước số nguyên tố bậc hai (ước số nguyên tố có mũ 2)
    for i in range(2, max_root + 1):
        if i * i <= N:
            count += 1

    # Đếm số ước số nguyên tố bậc ba (ước số nguyên tố có mũ 3)
    for i in range(2, max_cube_root + 1):
        if i * i * i <= N:
            count += 1

    return count

# Đọc giá trị N từ input
N = int(input())

# Gọi hàm để đếm số lượng số thỏa mãn yêu cầu
result = count_numbers_with_9_divisors(N)

# In ra kết quả
print(result)
