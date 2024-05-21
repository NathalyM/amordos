from tkinter import font, messagebox
from tkinter import *
import random

def obvio():
    messagebox.showinfo(message="Lo sabia", title="Título")

def button_hover(event):
    x = random.randint(10, 400)
    y = random.randint(10, 400)
    button_2.place(x=x, y=y)

def exit_(event):
    x = random.randint(10, 400)
    y = random.randint(10, 400)
    button_2.place(x=x, y=y)

root = Tk()
root.geometry("600x400")
root.configure(background='#f5c1dc')
root.title('RESPONDEME')

label_0 = Label(root, text="¿ME AMAS?", bg='#f5c1dc', fg='black', width=0, font=("BubbleGum", 30))
label_0.place(x=90, y=60)

button_1 = Button(root, text="NO", bg='#cc1f04', fg='white', width=5, font=("BubbleGum", 30), command=obvio)
button_1.place(x=100, y=220)

button_2 = Button(root, text="SI", bg='#cc1f04', fg='white', width=5, font=("BubbleGum", 30))
button_2.place(x=350, y=220)

button_2.bind('<Enter>', button_hover)
button_2.bind('<Leave>', exit_)

root.mainloop()