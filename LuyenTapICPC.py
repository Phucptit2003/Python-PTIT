while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    if n < m:
        n, m = m, n

    strength_increase = (n * (n + 1) // 2) - (m * (m + 1) // 2)
    print(strength_increase)
