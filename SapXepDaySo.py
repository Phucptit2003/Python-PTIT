def insert_max_value(arr, m):
    max_value = max(arr)
    max_index = arr.index(max_value)
    arr.insert(max_index, m)

# Hàm sắp xếp lại dãy số
def sort_array(arr):
    negative_numbers = [x for x in arr if x < 0]
    non_negative_numbers = [x for x in arr if x >= 0]
    return negative_numbers + non_negative_numbers

# Đọc số bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    insert_max_value(arr, m)

    sorted_arr = sort_array(arr)

    print(*sorted_arr)
