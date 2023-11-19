import math

# Hàm tính ƯCLN của một danh sách số
def calculate_gcd(arr):
    result_gcd = arr[0]
    for i in range(1, len(arr)):
        result_gcd = math.gcd(result_gcd, arr[i])
    return result_gcd

# Hàm tìm dãy con ngắn nhất với ƯCLN bằng k
def find_shortest_subarray_with_gcd(arr, k):
    n = len(arr)
    if n == 1 and arr[0] == k:
        return 1

    left = 0
    right = 0
    current_gcd = arr[0]
    min_length = n + 1

    while right < n:
        if current_gcd == k:
            min_length = min(min_length, right - left + 1)
            current_gcd //= arr[left]
            left += 1
            if left > right:
                right += 1
                if right < n:
                    current_gcd = arr[right]
        else:
            right += 1
            if right < n:
                current_gcd = math.gcd(current_gcd, arr[right])

    if min_length == n + 1:
        return -1
    return min_length


    
test = int(input())
for _ in range(test):
    n, k = map(int, input().split())
    arr = []
    while len(arr)<n:
        s=input().split()
        for i in s:
            arr.append(int(i))

    print(find_shortest_subarray_with_gcd(arr,k))
    
