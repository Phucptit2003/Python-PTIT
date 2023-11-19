import turtle
from tkinter import *
from tkinter.ttk import Style

Style=('Courier',25,'italic')

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("pink")
turtle.color('pink','pink')
turtle.goto(0,70)
turtle.pensize(5)
turtle.title("Phucdepzai")
def love():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.speed(0)
t.begin_fill()
t.color("red","red")
t.left(140)
t.forward(111.65)
love()

t.left(120)
love()
t.forward(111.65)
t.end_fill()
t.hideturtle()


turtle.color('black','pink')
turtle.write('NGA',font=Style,align='center')
turtle.hideturtle()
turtle.mainloop()

root.mainloop()