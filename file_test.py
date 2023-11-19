import tkinter as tk
from tkinter import ttk
import easyocr

# Khởi tạo Tkinter
root = tk.Tk()
root.title("Nhận dạng hình ảnh")

# Tạo Text widget
text_entry1 = tk.Text(root, width=40, height=10)
text_entry1.pack()

# Hàm nhận dạng và đưa chữ vào text widget
def recognize_and_insert_text():
    # Khởi tạo easyocr
    reader = easyocr.Reader(['en'])  # Chọn ngôn ngữ bạn muốn nhận dạng

    image = 'text_pic.jpg'  # Đường dẫn đến hình ảnh bạn muốn nhận dạng

    result = reader.readtext(image)
    recognized_text = ""
    for (bbox, text, prob) in result:
        recognized_text += text + " "  # Nối tất cả các từ đã nhận dạng lại

    text_entry1.insert("1.0", recognized_text)  # Đưa chữ vào text widget
    text_entry1.config(wrap="word") 
# Tạo nút để kích hoạt nhận dạng
recognize_button = ttk.Button(root, text="Nhận dạng và Đưa vào Text", command=recognize_and_insert_text)
recognize_button.pack()

root.mainloop()
