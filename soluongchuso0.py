def count_zeros_in_number(number, divisor):
    count = 0
    while number % divisor == 0:
        number //= divisor
        count += 1
    return count

def max_zeros_in_combinations(arr, k):
    cnt2_arr = [count_zeros_in_number(num, 2) for num in arr]
    cnt5_arr = [count_zeros_in_number(num, 5) for num in arr]

    n = len(arr)
    maxx = 0

    for mask in range(1 << n):
        if bin(mask).count('1') == k:
            cnt10 = 0
            cnt2 = 0
            cnt5 = 0
            for i in range(n):
                if mask & (1 << i):
                    cnt10 += count_zeros_in_number(arr[i], 10)
                    cnt2 += cnt2_arr[i]
                    cnt5 += cnt5_arr[i]
            
            maxx = max(maxx, cnt10 + min(cnt2, cnt5))

    return maxx

# Sử dụng hàm max_zeros_in_combinations
n, k = map(int, input().split())
input_string = input()
arr = list(map(int, input_string.split()))

result = max_zeros_in_combinations(arr, k)
print(result)
