import math

# Hàm kiểm tra xem có tồn tại dãy con có ước số chung lớn nhất bằng K không
def has_subarray_with_gcd(arr, K, length):
    current_gcd = arr[0]
    count = 1

    for i in range(1, length):
        current_gcd = math.gcd(current_gcd, arr[i])
        
        if current_gcd == K:
            count += 1
        
        if count == length:
            return True
    
    for i in range(length, len(arr)):
        current_gcd = math.gcd(current_gcd, arr[i])
        
        if current_gcd == K:
            return True
        
    return False

def find_min_length_subarray(arr, K):
    left, right = 1, len(arr)
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if has_subarray_with_gcd(arr, K, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    min_length = find_min_length_subarray(A, K)
    print(min_length)
