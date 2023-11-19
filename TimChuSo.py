def find_first_two_digits(n):
    a = [0, 2]
    b = [1, 1]

    for i in range(2, n + 1):
        a.append(2 * a[i - 1] + 2 * b[i - 1])
        b.append(a[i - 1] + b[i - 1])

    result = a[n]
    return result

# Đọc số lượng bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    n = int(input())
    result = find_first_two_digits(n)
    print("{:02}".format(result))
