import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ tệp CSV
flights = pd.read_csv('flights.csv')

# Tìm giá trị lớn nhất, nhỏ nhất, và trung bình theo tên cột
column_name = input("Nhập tên cột: ")
max_value = flights[column_name].max()
min_value = flights[column_name].min()
mean_value = flights[column_name].mean()

# Hiển thị thông tin thống kê
print(f"Giá trị lớn nhất của '{column_name}': {max_value}")
print(f"Giá trị nhỏ nhất của '{column_name}': {min_value}")
print(f"Giá trị trung bình của '{column_name}': {mean_value}")

# Vẽ biểu đồ scatter
plt.scatter(flights.index, flights[column_name])
plt.xlabel('Index')
plt.ylabel(column_name)
plt.title(f'Scatter Plot of {column_name}')
plt.show()

# Đọc dữ liệu từ tệp CSV
salaries = pd.read_csv('Salaries.csv')

# Biểu đồ thống kê sex
plt.figure(figsize=(6, 6))
sns.countplot(x='sex', data=salaries)
plt.xlabel('Giới tính')
plt.ylabel('Số lượng')
plt.title('Biểu đồ thống kê giới tính')
plt.show()

# Đọc dữ liệu từ tệp dữ liệu cần sắp xếp
data = pd.read_csv('Salaries.csv')

# Nhập tên cột để sắp xếp
column_name = input("Nhập tên cột để sắp xếp: ")

# Sắp xếp dữ liệu theo cột được nhập
sorted_data = data.sort_values(by=column_name)

# Vẽ biểu đồ
plt.figure(figsize=(12, 6))
plt.plot(sorted_data[column_name], label=column_name)
plt.xlabel('Index')
plt.ylabel(column_name)
plt.title(f'Sorted Data by {column_name}')
plt.legend()
plt.show()
