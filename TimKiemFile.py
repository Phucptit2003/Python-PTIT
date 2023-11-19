import fnmatch

# Đọc định dạng từ input
pattern = input().strip()

# Đọc số file từ input
N = int(input().strip())

# Đọc danh sách các file từ input và lưu vào một danh sách
file_list = []
for _ in range(N):
    file_list.append(input().strip())

# Duyệt qua từng file trong danh sách và kiểm tra xem file có phù hợp với định dạng không
for file_name in file_list:
    if fnmatch.fnmatch(file_name, pattern):
        print(file_name)
