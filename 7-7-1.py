def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_numbers(arr):
    prime_set = set()
    result = []
    for num in arr:
        if is_prime(num):
            prime_set.add(num)
    prime_list = sorted(list(prime_set))
    for prime in prime_list:
        result.append(str(prime))
    return ' '.join(result)

# Nhập số phần tử của mảng
n = int(input())

# Nhập các phần tử của mảng
arr = list(map(int, input().split()))

# Tìm và in ra các số nguyên tố trong mảng
print(find_prime_numbers(arr))
