def maximize_number(N, K):
    stack = []

    for digit in N:
        while K > 0 and stack and stack[-1] < digit:
            stack.pop()
            K -= 1
        stack.append(digit)


    while K > 0:
        stack.pop()
        K -= 1

    result = ''.join(stack)
    return result

# Đọc input
N = input().strip()
K = int(input().strip())


result = maximize_number(N, K)
print(result)
