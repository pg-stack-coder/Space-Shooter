import tkinter as tk
from tkinter import ttk
screen=tk.Tk( )
screen.geometry('600x600')
screen.title('challenge 1')
screen.config(bg='light blue')
items=['ice','green','hoi']
combovar=tk.StringVar(value=items[0])
combo=ttk.Combobox(screen,textvariable=combovar)
combo['values']=items
combo.pack()
combo.bind('<<Combobox Selected>>',lambda event: label.config(text=f'Selected item:{combovar.get()}'))
label=tk.Label(textvariable=combovar)
label.pack()
spin=ttk.Spinbox(screen,from_=1 ,to=20,increment=2)
spin.bind('<<Increment>>',lambda event: print('up'))
spin.bind('<<Decrement>>',lambda event: print('down'))
spin.pack()
screen.mainloop()