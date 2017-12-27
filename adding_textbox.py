import Tkinter as tk
import ttk
from Tkinter import Text

def click_me():
    action.configure(text="hello:" + name.get())

prt=tk.Tk()
prt.title("hello this is textbox demo:")
ttk.Label(prt,text="enter your name:").grid(column=0,row=0)

name=tk.StringVar()
name_entered=ttk.Entry(prt, width=13, textvariable=name)
name_entered.focus()
#name_entered.set(name)
#name_entered.pack()
name_entered.grid(column=0,row=1)
action=ttk.Button(prt,text='click me',command=click_me)
action.grid(column=1,row=1)

tk.mainloop()



