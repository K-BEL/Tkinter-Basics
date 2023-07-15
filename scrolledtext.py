from tkinter import *

from tkinter import scrolledtext

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

txt = scrolledtext.ScrolledText(window,width=40,height=10)

txt.grid(column=0,row=0)

txt.insert(INSERT,'You text goes here')

txt.delete(1.0,END)

window.mainloop()