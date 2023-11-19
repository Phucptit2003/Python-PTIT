import tkinter as tk

# Hàm tính tổng
def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 + num2)

# Hàm tính hiệu
def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 - num2)

# Hàm tính tích
def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 * num2)

# Hàm tính thương
def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 == 0:
        result.set("Không thể chia cho 0")
    else:
        result.set(num1 / num2)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Máy Tính Cá Nhân")

# Khung nhập số thứ nhất
label1 = tk.Label(root, text="Số thứ nhất:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

# Khung nhập số thứ hai
label2 = tk.Label(root, text="Số thứ hai:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Kết quả

result = tk.StringVar()
result.set("Kết quả")
label_result = tk.Label(root, textvariable=result)
label_result.pack()


# Các nút tính toán
add_button = tk.Button(root, text="Cộng", command=add)
subtract_button = tk.Button(root, text="Trừ", command=subtract)
multiply_button = tk.Button(root, text="Nhân", command=multiply)
divide_button = tk.Button(root, text="Chia", command=divide)
add_button.pack()
subtract_button.pack()
multiply_button.pack()
divide_button.pack()

# Khởi chạy ứng dụng
root.mainloop()
