import tkinter as tk
from tkinter import ttk
screen=tk.Tk()
screen.geometry('600x600')
screen.title('challenge 1')
screen.config(bg='light blue')
label=tk.Label(screen,text='mylabel',bg='yellow')
label.pack()
entry=ttk.Entry()
entry.pack()
def dace():
    print(entry.get())
button=tk.Button(screen,text=':)',command=dace,bg='red')
button.pack()
screen.mainloop()