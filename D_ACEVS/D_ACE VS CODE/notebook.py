import tkinter as tk
from tkinter import ttk
screen=tk.Tk( )
screen.geometry('600x600')
screen.title('challenge 1')

nb=ttk.Notebook()
tab1=ttk.Frame(nb,)
tab2=ttk.Frame(nb,)

button=tk.Button(tab1,text='button1')
button2=tk.Button(tab2,text='button2')
button.pack()
button2.pack()
nb.add(tab1,text='i j')
nb.add(tab2,text='mn')
nb.pack()
screen.mainloop()