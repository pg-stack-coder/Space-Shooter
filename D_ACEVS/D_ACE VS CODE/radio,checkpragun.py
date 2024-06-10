import tkinter as tk
from tkinter import ttk
screen=tk.Tk()
screen.geometry('600x600')
screen.title('challenge 1')
screen.config(bg='light blue')
chkvar=tk.BooleanVar()
radiovar=tk.StringVar(value='radio buutton')
check=ttk.Checkbutton(text='check',variable=chkvar,command= lambda:print(radiovar))
check.pack()
def radio():
    print(chkvar.get())
    chkvar.set(False)
radio1=ttk.Radiobutton(text='radio 1',variable=radiovar,value='A',command=radio)
radio2=ttk.Radiobutton(variable=radiovar,text='radio2',value='B',command=radio)
radio1.pack()
radio2.pack()
screen.mainloop()