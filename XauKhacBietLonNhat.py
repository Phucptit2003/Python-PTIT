# Đọc dữ liệu đầu vào
V = input()
s = input()
q = int(input())

# Tạo danh sách lưu vị trí xuất hiện đầu tiên của các ký tự trong s
positions = {}
for i, char in enumerate(s):
    if char not in positions:
        positions[char] = i

# Tạo danh sách lưu vị trí xuất hiện đầu tiên của các ký tự trong tập V
min_positions = {}
for char in V:
    min_positions[char] = 10**7

for i, char in enumerate(s):
    if char in min_positions:
        min_positions[char] = min(min_positions[char], i)

# Kiểm tra từng truy vấn
for _ in range(q):
    query = input()
    is_smallest_distinct = all(positions[char] < min_positions[char] for char in query)
    
    if is_smallest_distinct:
        print("YES")
    else:
        print("NO")
