import re

# Hàm kiểm tra xem một chuỗi có phải là địa chỉ IPv4 hợp lệ hay không
def is_valid_ipv4(s):
    # Kiểm tra số phần chia chuỗi theo dấu chấm
    parts = s.split('.')
    if len(parts) != 4:
        return False

    # Kiểm tra từng phần
    for part in parts:
        # Phần phải là số nguyên
        if not re.match(r'^\d+$', part):
            return False

        # Phải nằm trong khoảng từ 0 đến 255
        num = int(part)
        if num < 0 or num > 255:
            return False

        # Phần không được bắt đầu bằng số 0 (ngoại trừ trường hợp số 0)
        if num != 0 and part[0] == '0':
            return False

    return True

# Đọc số lượng bộ test
T = int(input())

# Kiểm tra từng bộ test
for _ in range(T):
    s = input()
    if is_valid_ipv4(s):
        print("YES")
    else:
        print("NO")
