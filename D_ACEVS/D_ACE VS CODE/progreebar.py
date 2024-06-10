import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as scr
screen=tk.Tk( )
screen.geometry('600x600')
screen.title('challenge 1')
frame=ttk.Frame(screen,)
frame.pack(fill='both',expand=True)

float_var=tk.IntVar()
label=ttk.Label(frame,textvariable=float_var)
scale=ttk.Scale(frame,orient='vertical',variable=float_var,from_=0,to= 100)
bar=ttk.Progressbar(frame,orient='horizontal',maximum=100,variable=float_var)
scrtxt=scr.ScrolledText(width=600,height=700)
scrtxt.pack()
bar.start()
bar.pack()
label.pack()
scale.pack()
screen.mainloop()
