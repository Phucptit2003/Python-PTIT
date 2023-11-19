def count_largest_occurrences(N, steps):
    max_val = 0
    max_occurrences = 0
    count = [0]*(pow(10,6)+1)  # Tạo mảng đếm, bắt đầu từ index 1

    for a, b in steps:
        count[a] += 1
        count[b + 1] -= 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]
        if count[i] > max_val:
            max_val = count[i]
            max_occurrences = 1
        elif count[i] == max_val:
            max_occurrences += 1

    return max_occurrences

# Đọc input từ bàn phím
N = int(input())
steps = []
for _ in range(N):
    a, b = map(int, input().split())
    steps.append((a, b))

# Tìm và in ra kết quả
result = count_largest_occurrences(N, steps)
print(result)
