from tkinter import *
from tkinter import Menu
window = Tk()

window.title("first window")

window.geometry('450x300')

lbl = Label(window, text="Hello", font=("Arial Bold", 50))

lbl.grid(column=0, row=0)

txt = Entry(window,width=10) # txt = Entry(window,width=10, state='disabled')

txt.grid(column=1, row=0)

txt.focus() # Set focus to entry widget

def clicked():

    res = "Welcome to " + txt.get()

    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=0)


menu = Menu(window)

menu.add_command(label='File')

window.config(menu=menu)

window.mainloop()