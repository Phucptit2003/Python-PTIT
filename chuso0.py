def count_trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

def find_smallest_M_with_N_trailing_zeros(N):
    left, right = 5, 5 * N

    while left <= right:
        mid = (left + right) // 2
        zeros_count = count_trailing_zeros(mid)
        
        if zeros_count > N:
            right = mid - 1
        else:
            left = mid + 1

    return right
test=int(input())
for _ in range(test):
    N=int(input())
    result_M = find_smallest_M_with_N_trailing_zeros(N)
    print("{}".format(result_M))
