def count_digits_in_range(A, B):
    # Khởi tạo mảng đếm tần số xuất hiện của các chữ số từ 0 đến 9
    digit_count = [0] * 10

    # Chuyển A và B thành chuỗi để xác định độ dài của chúng
    len_A = len(str(A))
    len_B = len(str(B))

    # Duyệt qua từng chữ số từ len_A đến len_B
    for length in range(len_A, len_B + 1):
        for digit in range(1 if length == len_A else 0, 10):
            # Tính số lần xuất hiện của chữ số digit ở vị trí length
            count = 10 ** (length - 1) if digit == 0 else 10 ** (length - 1 - len_A)
            digit_count[digit] += count

    # In ra tần số đếm của các chữ số từ 0 đến 9
    for i in range(10):
        print(digit_count[i], end=" ")
    print()

# Đọc số lượng bộ test
T = int(input())

# Đọc và xử lý từng bộ test
for _ in range(T):
    A, B = map(int, input().split())
    count_digits_in_range(A, B)
