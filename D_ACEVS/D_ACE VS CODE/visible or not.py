import tkinter as tk
from tkinter import ttk
screen=tk.Tk( )
screen.geometry('600x600')
screen.title('challenge 1')
def toggle_fun():
    global labelvis
    if labelvis:
        label.place_forget()
        labelvis=False
    else:
        labelvis=True
        label.place(x=100,y=100,anchor='center')
labelvis=True
label=tk.Label(text='label')
label.place(x=100,y=100,anchor='center')
button=tk.Button(screen,text='toggle button',bg='green',command=toggle_fun)
button.pack(side='bottom')
screen.mainloop()
