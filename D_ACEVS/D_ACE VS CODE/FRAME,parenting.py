import tkinter as tk
from tkinter import ttk
screen=tk.Tk( )
screen.geometry('600x600')
screen.title('challenge 1')

frame=ttk.Frame(screen,width=400,height=400,borderwidth=10,relief=tk.RAISED)
button=tk.Button(frame,text='button1',bg='yellow')
# frame.pack_propagate()
frame.pack()
button.pack(expand=True,fill='both')
screen.mainloop()
