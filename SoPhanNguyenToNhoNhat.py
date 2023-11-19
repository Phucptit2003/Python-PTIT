# Hàm kiểm tra xem một số có phải là số nguyên tố hay không
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Hàm tìm số phản nguyên tố bé nhất không nhỏ hơn X
def find_smallest_semiprime(X):
    current_num = X
    while True:
        divisors_count = 0
        for i in range(1, current_num + 1):
            if current_num % i == 0:
                divisors_count += 1
            if divisors_count > 4:
                break
        if divisors_count == 4 and not is_prime(current_num):
            return current_num
        current_num += 1

# Đọc số bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    X = int(input())
    result = find_smallest_semiprime(X)
    print(result)
