# Đọc dữ liệu đầu vào
N = int(input())
A = list(map(int, input().split()))

# Tạo danh sách các cặp (giá trị, vị trí)
pairs = [(A[i], i) for i in range(len(A))]

# Sắp xếp danh sách các cặp theo giá trị giảm dần
pairs.sort(reverse=True, key=lambda x: x[0])

# Lưu lại vị trí của N cặp có giá trị lớn nhất
positions_to_keep = [pair[1] for pair in pairs[:N]]

# Sắp xếp danh sách các cặp theo vị trí ban đầu
positions_to_keep.sort()

# Trả về các phần tử ứng với vị trí đã lưu lại
result = [A[i] for i in positions_to_keep]

# In ra kết quả
print(result)
