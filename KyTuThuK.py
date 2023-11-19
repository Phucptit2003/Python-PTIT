def find_char_in_step(N, K):
    if N == 1:
        return 'A'

    middle = 2**(N - 1)
    if K == middle:
        return chr(ord('A') + N - 1)

    if K < middle:
        return find_char_in_step(N - 1, K)
    
    return find_char_in_step(N - 1, K - middle)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    result = find_char_in_step(N, K)
    print(result)
