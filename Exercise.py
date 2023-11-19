import pandas as pd
import matplotlib.pyplot as plt

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
#flights = pd.read_csv('flights.csv')

# Chuyển cột "date" sang kiểu datetime
flights['date'] = pd.to_datetime(flights['date'])

# Vẽ biểu đồ biến thiên ngày tháng và distance
plt.figure(figsize=(12, 6))
plt.plot(flights['date'], flights['distance'])
plt.xlabel('Ngày')
plt.ylabel('Khoảng cách')
plt.title('Biểu đồ biến thiên ngày tháng và distance')
plt.show()
