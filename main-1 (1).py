import tkinter as tk
from tkinter import *
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Translate")
root.geometry("720x480")
root.resizable(False, False)

#tạo nền
framel = Frame(root, width = 720, height = 480, relief=RIDGE, bg="#F0EDE6")
framel.place(x = 0, y = 0)

#tạo khung label
Label(root, text="Translator", font=("Helvetica 20"), fg = "#2C323E", bg = "#FAF4F6").pack(pady = 10)

#tạo ô select source_language
a = StringVar()
source_language = ttk.Combobox(framel, width=27, textvariable= a, state="randomly", font=("verdana", 10, "bold"))

source_language["value"] = (
    "tiếng Việt",
    "tiếng Anh",
    "tiếng Nga",
    "tiếng Trung"
)

source_language.place(x = 15, y = 50)
source_language.current(0)

# tạo ô select target_language
b = StringVar()
target_language = ttk.Combobox(framel, width=27, textvariable= b, state="randomly", font=("verdana", 10, "bold"))

target_language["value"] = (
    "tiếng Anh",
    "tiếng Nga",
    "tiếng Trung",
    "tiếng Việt"
)

target_language.place(x = 438, y = 50)
target_language.current(0)

#khung nhập văn bản dịch
text_entry1 = Text(framel, width = 25, height = 6, borderwidth = 2, relief=GROOVE, font=("verdana", 15))
text_entry1.place(x = 10, y = 80)

text_entry2 = Text(framel, width = 25, height = 6, borderwidth = 2, relief=GROOVE, font=("verdana", 15), bg = "#F5F5F5")
text_entry2.place(x = 380 , y = 80)

# đặt kích thước icon
newsize = (12, 12)
newsize_trans = (25, 25)

#icon nút dịch
translate_icon_image = Image.open("D:/hoctapreal/Năm 3/kì 1/PYTHON LEARN/BTL/BTL-Python/img+font/icon/translate_icon.png")
translate_icon_image = translate_icon_image.resize(newsize_trans, Image.ADAPTIVE)
translate_icon = ImageTk.PhotoImage(translate_icon_image)
#nút dịch
btn1 = Button(framel, text = "",image=translate_icon, compound="center", relief=RAISED, font=("verdana", 10, "bold"), bg = "#248AA2", fg = "white", cursor="hand2")
btn1.place(x = 344, y = 140)
#nút dịch tôi đang tính để hình cái icon mũi tên

#icon nút xoá
clear_icon_image = Image.open("D:/hoctapreal/Năm 3/kì 1/PYTHON LEARN/BTL/BTL-Python/img+font/icon/clear_icon.png")
clear_icon_image = clear_icon_image.resize(newsize, Image.ADAPTIVE)
clear_icon = ImageTk.PhotoImage(clear_icon_image)

#nút xoá
btn2 = Button(framel, text = " Xóa",image=clear_icon, compound="left", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg = "#248AA2", fg = "white", cursor="hand2")
btn2.place(x = 290, y = 250)


#icon phát tiếng
volume_icon_image = Image.open("D:/hoctapreal/Năm 3/kì 1/PYTHON LEARN/BTL/BTL-Python/img+font/icon/volume_icon.png")
volume_icon_image = volume_icon_image.resize(newsize, Image.ADAPTIVE)
volume_icon = ImageTk.PhotoImage(volume_icon_image)
# nút "Phát Tiếng"
play_button = Button(framel, text = " Phát Tiếng",image=volume_icon, compound="left", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg = "#248AA2", fg = "white", cursor="hand2")
play_button.place(x = 380, y = 250)

#icon thu âm
record_icon_image = Image.open("D:/hoctapreal/Năm 3/kì 1/PYTHON LEARN/BTL/BTL-Python/img+font/icon/record_icon.png")
record_icon_image = record_icon_image.resize(newsize, Image.ADAPTIVE)
record_icon = ImageTk.PhotoImage(record_icon_image)
# nút "Thu âm"
record_button = Button(framel, text = " Thu Âm", image=record_icon,compound="left", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg = "#248AA2", fg = "white", cursor="hand2")
record_button.place(x = 10, y = 250)

#icon dừng thu âm
record_stop_icon_image = Image.open("D:/hoctapreal/Năm 3/kì 1/PYTHON LEARN/BTL/BTL-Python/img+font/icon/record_stop_icon.png")
record_stop_icon_image = record_stop_icon_image.resize(newsize, Image.ADAPTIVE)
record_stop_icon = ImageTk.PhotoImage(record_stop_icon_image)
# nút "Dừng thu âm"
stop_record_button = Button(framel, text = " Dừng thu Âm",image=record_stop_icon, compound="left", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg = "#248AA2", fg = "white", cursor="hand2")
stop_record_button.place(x = 10, y = 280)


# Tạo lịch sử lịch
history_label = tk.Label(root, text="Lịch Sử Dịch:")
history_label.pack()
history_label.place(x = 320, y = 290)

history_text = tk.Text(root, height = 8, width = 48)
history_text.pack()
history_text.place(x = 170, y = 310)

root.mainloop()