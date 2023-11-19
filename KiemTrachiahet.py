
def count_coprime_numbers(L, R, N):
    coprimes = [1] * (R - L + 1)
    for i in range(2, N + 1):
        if i > R:
            break
        multiple = (L // i) * i
        while multiple <= R:
            if multiple >= L and multiple != i:
                coprimes[multiple - L] = 0
            multiple += i

    count = sum(coprimes)
    return count



while True:
    arr=[int(x) for x in input().split()]
    if arr[0] == -1:
        break
    L= arr[0]
    R= arr[1]
    N = int(input())
    count = count_coprime_numbers(L,R,N)
    
    print(count)
