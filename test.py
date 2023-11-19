import tkinter as tk
from tkinter import *
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
import os
import pyaudio
import pygame
from PIL import Image, ImageTk
import speech_recognition as sr
from tkinter import filedialog
import easyocr
import pyttsx3
from gtts import gTTS



# Khai báo biến
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 44100
chunk = 1024
recording = False
audio_data = []
translation_history = []
# Khởi tạo recognizer
recognizer = sr.Recognizer()


def recognize_speech():
    global is_translated
    global source_language_var
    file_path = filedialog.askopenfilename(filetypes=[("Wave files", "*.wav")])
    if file_path:
        if file_path.lower().endswith(".wav") and os.path.isfile(file_path):
            with sr.AudioFile(file_path) as source:
                audio_data = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio_data, language=source_language_var.get())
                    text_entry1.delete("1.0", "end")
                    text_entry1.insert("1.0", text)
                    is_translated = True
                except sr.UnknownValueError:
                    messagebox.showinfo("Thông báo", "Không thể nhận dạng giọng nói. Vui lòng thử lại.")
                except sr.RequestError:
                    messagebox.showinfo("Thông báo", "Có lỗi xảy ra trong quá trình nhận dạng giọng nói. Vui lòng thử lại.")
        else:
            messagebox.showinfo("File không hợp lệ")
# Hàm nhận dạng và đưa chữ vào text widget
def recognize_and_insert_text():
    global source_language_var
    source_language = source_language_var.get()
    # Khởi tạo easyocr
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.JPG;*.jpeg;*.gif;*.bmp")])

    if file_path:
        # Khởi tạo easyocr
        reader = easyocr.Reader([source_language])  # Chọn ngôn ngữ bạn muốn nhận dạng

        result = reader.readtext(file_path)
        recognized_text = ""
        for (bbox, text, prob) in result:
            recognized_text += text + " "  # Nối tất cả các từ đã nhận dạng lại

        text_entry1.insert("1.0", recognized_text)  # Đưa chữ vào text widget
        text_entry1.config(wrap="word")

#
def speak_text_source():
    global source_language_var
    global text_entry1
    language = source_language_var.get()
    text = text_entry1.get("1.0", "end-1c")
    print(language)
    print(text)

    if language == "en":
        engine = pyttsx3.init(driverName="sapi5")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    elif language == "vi":
        output = gTTS(text, lang="vi", slow=False)
        output.save('output1.mp3')  # Lưu tệp âm thanh với tên 'output1.mp3'
        # Khởi tạo pygame
        pygame.init()

        # Tên của tệp âm thanh MP3 bạn muốn phát
        audio_file = "output1.mp3"

        # Tạo một đối tượng âm thanh
        pygame.mixer.music.load(audio_file)

        # Phát âm thanh
        pygame.mixer.music.play()

        # Đợi cho đến khi âm thanh phát xong
        # Chờ cho đến khi âm thanh phát xong
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10) 

        # Kết thúc pygame
        pygame.quit()


def speak_text_target():
    global target_language_var
    global text_entry2
    language = target_language_var.get()
    text = text_entry2.get("1.0", "end-1c")
    print(language)
    print(text)

    if language == "en":
        engine = pyttsx3.init(driverName="sapi5")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    elif language == "vi":
        output = gTTS(text, lang="vi", slow=False)
        output.save('output.mp3')  # Lưu tệp âm thanh với tên 'output.mp3'
        # Khởi tạo pygame
        pygame.init()

        # Tên của tệp âm thanh MP3 bạn muốn phát
        audio_file = "output.mp3"

        # Tạo một đối tượng âm thanh
        pygame.mixer.music.load(audio_file)

        # Phát âm thanh
        pygame.mixer.music.play()

        # Đợi cho đến khi âm thanh phát xong
        # Chờ cho đến khi âm thanh phát xong
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Kết thúc pygame
        pygame.quit()
#

def update_history_text():
    history_text.delete("1.0", "end")  # Xóa nội dung cũ
    for entry in translation_history:
        text, translation = entry
        history_text.insert("end", f"Original: {text}\n\nTranslation: {translation}\n\n")

#
is_translated = False
def translate_text():
    global is_translated
    input_text = text_entry1.get("1.0", "end-1c")
    source_language = source_language_var.get()
    target_language = target_language_var.get()
    translator = Translator()
    translated_text = translator.translate(input_text, src=source_language, dest=target_language).text
    text_entry2.delete("1.0", "end")
    text_entry2.insert("1.0", translated_text)
    translation_history.append((input_text,translated_text))  # Thêm vào lịch sử dịch
    update_history_text()
    is_translated = True  

#ham clear 
def clear_text():
    global is_translated
    if is_translated:
        text_entry1.delete("1.0", "end")
        text_entry2.delete("1.0", "end")
        is_translated = False
    else:
        text_entry1.delete("1.0", "end")
        text_entry2.delete("1.0", "end")
        is_translated = False 


root = tk.Tk()
root.title("Translate")
root.geometry("1000x500+200+100")
root.resizable(False, False)
root.minsize(1000, 500)
root.iconbitmap('icon.ico') 


# Tạo nền
frame1 = Frame(root, width=1000, height=500, relief=RIDGE, bg="#F0EDE6")
frame1.place(x=0, y=0)
background = ImageTk.PhotoImage(Image.open("background.jpg"))
background_label = tk.Label(frame1, image=background)
background_label.place(relwidth=1, relheight=1)
background_label.photo = background

# Tạo ô select source_language
source = tk.Label(frame1, text="Ngôn ngữ nguồn", font=("Helvetica 15"), fg="#2c323e", bg="#F0EDE6")
source.place(x=150, y=20)
source_language_var = tk.StringVar()
source_language = ttk.Combobox(frame1, width=30, textvariable=source_language_var, state="readonly", font=("verdana", 10, "bold"))

source_language["value"] = (
    "auto",
    "en",
    "vi",
    
)

source_language.place(x=80, y=50)
source_language.current(0)

# Tạo ô select target_language
target = tk.Label(frame1, text="Ngôn ngữ đích", font=("Helvetica 15"), fg="#2c323e", bg="#F0EDE6")
target.place(x=700, y=20)
target_language_var = tk.StringVar()
target_language_var.set("en")

target_language = ttk.Combobox(frame1, width=30, textvariable=target_language_var, state="readonly",
                               font=("verdana", 10, "bold"))
target_language["value"] = (
    "auto",
    "en",
    "vi",
)
target_language.place(x=630, y=50)
target_language.current(0)

# Khung nhập văn bản dịch
text_entry1 = Text(frame1, width=35, height=7, borderwidth=2, relief=GROOVE, font=("verdana", 15))
text_entry1.place(x=10, y=80)
text_entry1.config(wrap="word") 

text_entry2 = Text(frame1, width=35, height=7, borderwidth=2, relief=GROOVE, font=("verdana", 15), bg="#F5F5F5")
text_entry2.place(x=530, y=80)
text_entry2.config(wrap="word") 
#chỉnh kích thước icon
newsize = (35, 35)
newsize_vol_file = (35, 35)
newsize_trans = (35, 35)
# Nút dịch
btn1_img = Image.open("translate_icon.png")
btn1_img = btn1_img.resize(newsize_trans, Image.ADAPTIVE)
btn1_icon = ImageTk.PhotoImage(btn1_img)
btn1 = Button(frame1, text=" ",image=btn1_icon, compound="center", relief=RAISED, font=("verdana", 10, "bold"), bg="#F0EDE6", fg="white",
             cursor="hand2", command=translate_text)
btn1.place(x=478, y=150)
# Nút dịch tôi đang tính để hình cái icon mũi tên

# Nút xoá
btn2_img = Image.open("clear_icon.png")
btn2_img = btn2_img.resize(newsize, Image.ADAPTIVE)
btn2_icon = ImageTk.PhotoImage(btn2_img)
btn2 = Button(frame1, text=" ",image=btn2_icon, compound="center", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"),
             bg="#F0EDE6", fg="white", cursor="hand2", command=clear_text)
btn2.place(x=427, y=270)

# Nút "volume target language"
volume_target_img = Image.open("volume_icon.png")
volume_target_img = volume_target_img.resize(newsize, Image.ADAPTIVE)
volume_target_icon = ImageTk.PhotoImage(volume_target_img)
play_button_target = Button(frame1, text=" ",image=volume_target_icon, compound="center", relief=RAISED, borderwidth=2,
                     font=("verdana", 10, "bold"),
                     bg="#F0EDE6", fg="white", cursor="hand2", command=speak_text_target)
play_button_target.place(x=530, y=270)

# Nút "volume source language"
volume_source_img = Image.open("volume_icon.png")
volume_source_img = volume_source_img.resize(newsize, Image.ADAPTIVE)
volume_source_icon = ImageTk.PhotoImage(volume_source_img)
play_button_source = Button(frame1, text=" ", image=volume_source_icon, compound="center", relief=RAISED, borderwidth=2,
                     font=("verdana", 10, "bold"),
                     bg="#F0EDE6", fg="white", cursor="hand2", command=speak_text_source)
play_button_source.place(x=10, y=270)

# Nút "Scan"
scan_img = Image.open("picture_icon.png")
scan_img = scan_img.resize(newsize_vol_file, Image.ADAPTIVE)
scan_icon = ImageTk.PhotoImage(scan_img)
scan_button = Button(frame1, text=" ", image=scan_icon, compound="center", relief=RAISED, borderwidth=2,
                      font=("verdana", 10, "bold"),
                      bg="#F0EDE6", fg="white", cursor="hand2", command=recognize_and_insert_text)
scan_button.place(x=10, y=350)

# Nút "Chọn file am thanh"
wav_img = Image.open("file_icon.png")
wav_img = wav_img.resize(newsize_vol_file, Image.ADAPTIVE)
wav_icon = ImageTk.PhotoImage(wav_img)
wav_button = Button(frame1, text=" ",image=wav_icon, compound="center", relief=RAISED, borderwidth=2,
                            font=("verdana", 10, "bold"), bg="#F0EDE6", fg="white", cursor="hand2",command=recognize_speech)
wav_button.place(x=70, y=350)

# Tạo lịch sử lịch
history_label = tk.Label(frame1, text="Lịch Sử Dịch:", font=("Helvetica 15"), fg="#2c323e", bg="#F0EDE6")
history_label.pack()
history_label.place(x=600, y=300)

history_text = Text(frame1, width=35, height=6, borderwidth=2, relief=GROOVE, font=("verdana", 15), bg="#F5F5F5")
history_text.pack()
history_text.place(x=530, y=330)
history_text.config(wrap="word")

root.mainloop()
