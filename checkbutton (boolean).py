from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome")

window.geometry('350x200')

chk_state = IntVar()

#chk_state.set(0) #uncheck

chk_state.set(1) #check #1 for the first i guess

chk1 = Checkbutton(window, text='Choose', var=chk_state)

chk1.grid(column=0, row=0)

window.mainloop()