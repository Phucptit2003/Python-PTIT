from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator
import googletrans
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("Minh's Translator")
root.geometry("1080x1024")
root.iconbitmap('4592.ico')

load = Image.open('mt.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x = 0, y = 0)

name = Label(root, text="Translator", fg = "#FFFFFF", bd=0,bg ="#386270" )
name.config(font=("Transformer Movie", 30))
name.pack(pady=10)

box=Text(root,width=28,height=8, font=("ROBOTO",16))
box.pack(pady=20)

button_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def clear1():
    box2.delete(1.0,END)
def translate():
    src = 'en'
    dest = 'vi'
    if (x.get()) == 0:
        src = 'en'
        dest = 'vi'
    elif(x.get()) == 1:
        src = 'vi'
        dest = 'en'
    else:
        pass
    input=box.get(1.0,END)
    print(input)
    t = Translator()
    a = t.translate(input, src = src, dest = dest)
    b = a.text
    box1.insert(END,b)
    box2.insert(END,b)
    
clear_button=Button(button_frame,text="Clear text",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=clear)
clear_button.place(x=400,y=300)
trans_button=Button(button_frame,text="Translate",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=translate)
trans_button.place(x=600,y=300)
box1=Text(root,width=28,height=8, font=("ROBOTO",16))
box1.pack(pady=30)

name1 = Label(root, text="History", fg = "#FFFFFF", bd=0,bg ="#3D7A8C" )
name1.config(font=("Transformer Movie", 20))
name1.pack(pady=5)
box2=Text(root,width=78,height=4, font=("ROBOTO",16))
box2.pack(pady=10)

clear_button=Button(button_frame,text="Clear History",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=clear1)
clear_button.place(x=500,y=730)

frame_option = LabelFrame(root, text = "Languages")
frame_option.place(x=800,y=300)
lang = ["English to Vietnamese", "Vietnamese to English"]
x = IntVar()
x.set("0")
for index in range(len(lang)):
    radiobutton = Radiobutton(frame_option, text = lang[index],variable=x,value=index, font='Arial 10')
    radiobutton.pack(anchor=W)

def dropdown_opened():
    print("The drop-down has been opened!")


combo = ttk.Combobox(
    values=["Vietnamese", "English", "Russian", "Chinese"],
    postcommand=dropdown_opened
)
combo.place(x=20, y=90)

combo2 = ttk.Combobox(
    values=["Vietnamese", "English", "Russian", "Chinese"],
    postcommand=dropdown_opened
)
combo2.place(x=200, y=90)

root.mainloop()