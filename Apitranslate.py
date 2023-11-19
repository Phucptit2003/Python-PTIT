import tkinter as tk
from googletrans import Translator
import pyttsx3

def translate_and_speak():
    text_to_translate = input_text.get("1.0", "end-1c")
    target_language = target_language_var.get()

    translator = Translator()
    translated_text = translator.translate(text_to_translate, dest=target_language)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", translated_text.text)

    # Phát âm thanh từ văn bản đã dịch
    engine = pyttsx3.init()
    engine.say(translated_text.text)
    engine.runAndWait()

app = tk.Tk()
app.title("Ứng dụng Dịch")

input_label = tk.Label(app, text="Nhập văn bản cần dịch:")
input_label.pack()
input_text = tk.Text(app, height=5, width=40)
input_text.pack()

target_language_var = tk.StringVar()
target_language_var.set("en")
target_language_label = tk.Label(app, text="Chọn ngôn ngữ đích:")
target_language_label.pack()
target_language_menu = tk.OptionMenu(app, target_language_var, "en", "fr", "es", "de")
target_language_menu.pack()

translate_button = tk.Button(app, text="Dịch", command=translate_and_speak)
translate_button.pack()

output_label = tk.Label(app, text="Kết quả dịch:")
output_label.pack()
output_text = tk.Text(app, height=5, width=40)
output_text.pack()


app.mainloop()
