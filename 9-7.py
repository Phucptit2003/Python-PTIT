# Nhập mảng số nguyên từ người dùng
n = int(input())
arr = []
for i in range(n):
    num = int(input(.format(i+1)))
    arr.append(num)

# Sắp xếp mảng theo thứ tự không giảm
arr.sort()

# Lấy 3 phần tử cuối cùng trong mảng
a, b, c = arr[-3:]

# Tính tích của 3 phần tử
product = a * b * c

# In giá trị tích lớn nhất
print( product)
