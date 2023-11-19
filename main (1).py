import tkinter as tk
from tkinter import *
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
import enchant
import os
import pyaudio
import wave
from pydub import AudioSegment
import threading 

# Tạo một từ điển cho kiểm tra chính tả
spell_checkers = {
    "en": enchant.Dict("en_US"),
    #"es": enchant.Dict("es_ES"),
    #"fr": enchant.Dict("fr_FR"),
    #"de": enchant.Dict("de_DE"),
    #"ja": enchant.Dict("ja_JP"),
    #"ko": enchant.Dict("ko_KR"),
    #"zh": enchant.Dict("zh_CN"),
    #"vi": enchant.Dict("vi_VN"),  # Thêm tiếng Việt (vi)
}

def translate_text():
    global is_translated
    input_text = text_entry1.get("1.0", "end-1c")
    source_language = source_language_var.get()
    target_language = target_language_var.get()

    # Kiểm tra chính tả dựa trên ngôn ngữ nguồn
    is_spelled_correctly = spell_checkers.get(source_language, enchant.Dict("en_US")).check(input_text)
    if not is_spelled_correctly:
        messagebox.showinfo("Thông báo", "Vui lòng kiểm tra lại chính tả của văn bản.")

    translator = Translator()
    translated_text = translator.translate(input_text, src=source_language, dest=target_language).text
    text_entry2.delete("1.0", "end")
    text_entry2.insert("1.0", translated_text)
    is_translated = True

def clear_text():
    global is_translated
    if is_translated:
        text_entry1.delete("1.0", "end")
        text_entry2.delete("1.0", "end")
        is_translated = False
    else:
        text_entry1.delete("1.0", "end")
        text_entry2.delete("1.0", "end")
        is_translated = False  # Thêm dòng này để đảm bảo biến is_translated được cập nhật
        
# Khai báo biến để theo dõi trạng thái thu âm
is_recording = False

# Hàm ghi âm từ máy tính trong một luồng con
def record_audio_thread():
    global is_recording
    audio = pyaudio.PyAudio()
    stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk)
    frames = []

    print("Bắt đầu ghi âm...")
    is_recording = True
    while is_recording:
        try:
            data = stream.read(chunk)
            frames.append(data)
        except KeyboardInterrupt:
            break

    print("Dừng ghi âm...")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(input_audio_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

# Hàm bắt đầu ghi âm
def start_recording():
    global recording_thread
    recording_thread = threading.Thread(target=record_audio_thread)
    recording_thread.start()

def stop_recording():
    global is_recording
    is_recording = False

# Hàm dịch văn bản và ghi âm khi nhấn nút "Phát Tiếng"
def translate_and_play_audio():
    translate_text()
    translated_text = text_entry2.get("1.0", "end-1c")

    # Ghi âm văn bản đã dịch
    tts = gTTS(text=translated_text, lang=target_language_var.get())
    tts.save(output_audio_file)

    # Phát âm thanh
    play_translated_audio()

# Hàm hiển thị âm thanh đã ghi vào ô
def display_recorded_audio():
    audio = AudioSegment.from_wav(input_audio_file)
    audio.export("recorded_audio.mp3", format="mp3")
    os.system("mpg123 recorded_audio.mp3")


root = tk.Tk()
root.title("Translate")
root.geometry("720x480")
root.resizable(False, False)

#tạo nền
framel = Frame(root, width=720, height=480, relief=RIDGE, bg="#F0EDE6")
framel.place(x=0, y=0)

#tạo khung label
Label(root, text="Translator", font=("Helvetica 20"), fg="#2C323E", bg="#FAF4F6").pack(pady=10)

#khung nhập văn bản dịch
text_entry1 = Text(framel, width=25, height=6, borderwidth=2, relief=GROOVE, font=("verdana", 15))
text_entry1.grid(row=2, column=0, padx=10, pady=10, rowspan=2)

text_entry2 = Text(framel, width=25, height=6, borderwidth=2, relief=GROOVE, font=("verdana", 15), bg="#F5F5F5")
text_entry2.grid(row=2, column=1, padx=10, pady=10, rowspan=2)

#nút dịch
btn1 = Button(framel, text=" ", relief=RAISED, font=("verdana", 10, "bold"), bg="#248AA2", fg="white", cursor="hand2", command=translate_text)
btn1.grid(row=3, column=2, padx=10, pady=10, rowspan=2)
#nút dịch tôi đang tính để hình cái icon mũi tên

#nút clear
btn2 = Button(framel, text="Xóa", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg="#248AA2", fg="white", cursor="hand2", command=clear_text)
btn2.grid(row=5, column=2, padx=10, pady=10)

# Danh sách thả xuống cho ngôn ngữ cần dịch
source_language_label = tk.Label(framel, text="Ngôn ngữ cần dịch:", font=("verdana", 12), bg="#F0EDE6")
source_language_label.grid(row=2, column=0, padx=10, pady=10)

source_language_var = tk.StringVar()
source_language_var.set("auto")

source_language_dropdown = ttk.Combobox(framel, textvariable=source_language_var, values=["auto", "en", "es", "fr", "de", "ja", "ko", "zh", "vi"])
source_language_dropdown.grid(row=2, column=1, padx=10, pady=10)

# Tạo một lớp Frame riêng để chứa danh sách thả xuống
language_frame = tk.Frame(framel, bg="#F0EDE6")
language_frame.place(x=10, y=220)

# Danh sách thả xuống cho ngôn ngữ muốn dịch đến
target_language_label = tk.Label(language_frame, text="Ngôn ngữ muốn dịch đến:", font=("verdana", 12), bg="#F0EDE6")
target_language_label.grid(row=2, column=79, padx=10, pady=10)

target_language_var = tk.StringVar()
target_language_var.set("en")

target_language_dropdown = ttk.Combobox(language_frame, textvariable=target_language_var, values=["en", "es", "fr", "de", "ja", "ko", "zh", "vi"])
target_language_dropdown.grid(row=2, column=80, padx=10, pady=10)


# Tạo nút "Phát Tiếng"
play_button = Button(framel, text="Phát Tiếng", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg="#248AA2", fg="white", cursor="hand2", command=translate_and_play_audio)
play_button.grid(row=4, column=0, padx=10, pady=10)

# Tạo nút "Thu Âm"
record_button = Button(framel, text="Thu Âm", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg="#248AA2", fg="white", cursor="hand2", command=start_recording)
record_button.grid(row=4, column=1, padx=10, pady=10)

# Tạo nút "Dừng Thu Âm"
stop_record_button = Button(framel, text="Dừng Thu Âm", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg="#248AA2", fg="white", cursor="hand2", command=stop_recording)
stop_record_button.grid(row=4, column=2, padx=10, pady=10)

# Tạo nút "Hiển thị Âm Thanh Ghi Âm"
display_audio_button = Button(framel, text="Hiển thị Âm Thanh Ghi Âm", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg="#248AA2", fg="white", cursor="hand2", command=display_recorded_audio)
display_audio_button.grid(row=4, column=3, padx=10, pady=10)


# Tạo lịch sử lịch
history_label = tk.Label(root, text="Lịch Sử Dịch:")
history_label.pack()
history_label.place(x = 320, y = 290)

history_text = tk.Text(root, height = 8, width = 48)
history_text.pack()
history_text.place(x = 170, y = 310)

root.mainloop()