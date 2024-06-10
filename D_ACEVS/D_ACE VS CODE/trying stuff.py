import tkinter as tk
import ttkbootstrap as tkk
screen=tk.Tk()
screen.geometry('600x600')
screen.title('challenge 1')
screen.config(bg='light blue')
ttk.window(themename='dark')
label=tk.Label(screen,text='mylabel',bg='yellow',font='Callibri 40')
label.pack()
#label.config(bg='green')
entry=ttk.Entry()
entry.pack()
def dace():
    print(entry.get())
button=tk.Button(screen,text=':)',command=dace,bg='red')
button.pack()
screen.mainloop()