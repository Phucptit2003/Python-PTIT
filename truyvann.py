def count_trailing_zeros(num):
    count = 0
    while num % 5 == 0:
        count += 1
        num //= 5
    return count

def find_smallest_factorial_with_zeros(n):
    current_zeros = 0
    M = 0

    while current_zeros < n:
        M += 1
        current_zeros += count_trailing_zeros(M)

    if current_zeros == n:
        return M
    else:
        return -1  

t=int(input())
arr=[]
for  _ in range(t):
    n=int(input())
    arr.append(n)
for i in arr:
    M = find_smallest_factorial_with_zeros(i)
    print(M)
