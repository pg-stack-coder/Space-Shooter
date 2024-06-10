import tkinter as tk
import tkinter as tkk
screen=tk.Tk()
screen.geometry('600x600')
screen.title('challenge 1')
screen.config(bg='light blue')
checkvar=tk.IntVar()
check=tk.Checkbutton(screen,variable=checkvar,onvalue=1,offvalue=0)
screen.mainloop()