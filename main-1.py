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
import playsound


# Khai báo biến
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 44100
chunk = 1024
audio_filename = "C:\\Users\\phucl\\Music\\test1.wav"
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
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

    if file_path:
        # Khởi tạo easyocr
        reader = easyocr.Reader(['en'])  # Chọn ngôn ngữ bạn muốn nhận dạng

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
            pygame.time.Clock().tick(10) # Đợi trong 5 giây (có thể điều chỉnh theo nhu cầu của bạn)

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
            pygame.time.Clock().tick(10)  # Đợi trong 5 giây (có thể điều chỉnh theo nhu cầu của bạn)

        # Kết thúc pygame
        pygame.quit()
#

def update_history_text():
    history_text.delete("1.0", "end")  # Xóa nội dung cũ
    for entry in translation_history:
        text, translation = entry
        history_text.insert("end", f"Original: {text}\nTranslation: {translation}\n\n")

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
root.geometry("720x480")

# Tạo nền
frame1 = Frame(root, width=720, height=480, relief=RIDGE, bg="#F0EDE6")
frame1.place(x=0, y=0)

# Tạo ô select source_language
source = tk.Label(frame1, text="Ngôn ngữ nguồn", font=("Helvetica 15"), fg="#2c323e", bg="#F0EDE6")
source.place(x=70, y=20)
source_language_var = tk.StringVar()
source_language = ttk.Combobox(frame1, width=27, textvariable=source_language_var, state="randomly", font=("verdana", 10, "bold"))

source_language["value"] = (
    "auto",
    "en",
    "vi",
    
)
#source_language_var.set("auto")

source_language.place(x=15, y=50)
source_language.current(0)

# Tạo ô select target_language
target = tk.Label(frame1, text="Ngôn ngữ đích", font=("Helvetica 15"), fg="#2c323e", bg="#F0EDE6")
target.place(x=500, y=20)
target_language_var = tk.StringVar()
target_language_var.set("en")

target_language = ttk.Combobox(frame1, width=27, textvariable=target_language_var, state="randomly",
                               font=("verdana", 10, "bold"))
target_language["value"] = (
    "auto",
    "en",
    "vi",
)
target_language.place(x=438, y=50)
target_language.current(0)

# Khung nhập văn bản dịch
text_entry1 = Text(frame1, width=25, height=6, borderwidth=2, relief=GROOVE, font=("verdana", 15))
text_entry1.place(x=10, y=80)
# Thiết lập tùy chọn wrap
text_entry1.config(wrap="word") 
#
text_entry2 = Text(frame1, width=25, height=6, borderwidth=2, relief=GROOVE, font=("verdana", 15), bg="#F5F5F5")
text_entry2.place(x=380, y=80)
# Thiết lập tùy chọn wrap
text_entry2.config(wrap="word") 
# Nút dịch
btn1 = Button(frame1, text="", compound="center", relief=RAISED, font=("verdana", 10, "bold"), bg="#248AA2", fg="white",
             cursor="hand2", command=translate_text)
btn1.place(x=344, y=140)
# Nút dịch tôi đang tính để hình cái icon mũi tên

# Nút xoá
btn2 = Button(frame1, text="Xóa", compound="left", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"),
             bg="#248AA2", fg="white", cursor="hand2", command=clear_text)
btn2.place(x=290, y=250)

# Nút "Phát Tiếng Dich"
play_button = Button(frame1, text="Phát Tiếng", compound="left", relief=RAISED, borderwidth=2,
                     font=("verdana", 10, "bold"),
                     bg="#248AA2", fg="white", cursor="hand2", command=speak_text_target)
play_button.place(x=380, y=250)

# Nút "Phát Nguon"
play_button_source = Button(frame1, text="Phát Tiếng", compound="left", relief=RAISED, borderwidth=2,
                     font=("verdana", 10, "bold"),
                     bg="#248AA2", fg="white", cursor="hand2", command=speak_text_source)
play_button_source.place(x=10, y=250)

# Nút "Scan"
record_button = Button(frame1, text="Scan picture", compound="left", relief=RAISED, borderwidth=2,
                      font=("verdana", 10, "bold"),
                      bg="#248AA2", fg="white", cursor="hand2", command=recognize_and_insert_text)
record_button.place(x=10, y=350)

# Nút "Chọn file am thanh"
stop_record_button = Button(frame1, text="Wav_file", compound="left", relief=RAISED, borderwidth=2,
                            font=("verdana", 10, "bold"), bg="#248AA2", fg="white", cursor="hand2",command=recognize_speech)
stop_record_button.place(x=10, y=380)

# Tạo lịch sử lịch
history_label = tk.Label(root, text="Lịch Sử Dịch:")
history_label.pack()
history_label.place(x=320, y=290)

history_text = tk.Text(root, height=8, width=48)
history_text.pack()
history_text.place(x=170, y=310)
history_text.config(wrap="word")

root.mainloop()
