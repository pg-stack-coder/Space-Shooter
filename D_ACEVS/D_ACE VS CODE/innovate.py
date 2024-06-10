import tkinter as tk
from tkinter import ttk
screen=tk.Tk()
screen.geometry('600x500')
def dace():
    screen2=tk.Tk()
    screen2.geometry('400x300')
    screen2.config(bg='red')
    label=tk.Label(master=screen2,text='HAPPY NEW YEAR',bg='orange')
    label.place(x=100,y=50,height=200,width=200)
def Dace():
    screen3=tk.Tk()
    screen3.geometry('400x300')
    screen3.config(bg='red')
    label=tk.Label(master=screen3,text='CHEER UP! ITS A NEW DAWN',bg='orange')
    label.place(x=100,y=50,height=200,width=200)
screen.title('D_ACE is here')
screen.config(bg='light blue')
button=tk.Button(master=screen,text=':)',command=dace,bg='yellow')
button.place(x=300,y=175,width=30,height=30)
button1=tk.Button(master=screen,text=':(',bg='yellow',command=Dace)
button1.place(width=30,height=30,x=300,y=210)
screen.mainloop()