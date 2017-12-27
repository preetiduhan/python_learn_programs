import Tkinter as tk
from Tkinter import *
import ttk
prt=tk.Tk()
prt.title("preeti first GUI program")
prt.resizable(0,0)
#Adding label to the interface
prt=ttk.Label(prt,text="username")
prt.grid(column=0 , row=0)

def click_me():
    action.configure(text="hello you have clicked me!!!!")
    print ('***************')
    prt.configure(foreground='red')
    print('*****************')

action=ttk.Button(prt,text='clickme!!',command=click_me)
action.grid(column=20,row=1)
tk.mainloop()
