import tkinter as tk
from tkinter import ttk
screen=tk.Tk()
screen.geometry('600x600')
screen.title('challenge 1')
screen.config(bg='light blue')
canvas=tk.Canvas(screen,bg='white')
canvas.pack()
#canvas.create_rectangle(20,40,50,200,fill='blue',width=5,dash=(1,4))
canvas.create_polygon(23,23,67,67,89,99,34,43)
canvas.create_line(23,45,78,90)
canvas.create_oval(65,110,20,155,fill='red')
canvas.create_arc(65,110,20,155,start=45,extent=180,style=tk.CHORD,outline='green',width=7,fill='green')
canvas.create_text(50,50,text='udgiesuwghdf',fill='blue',font='Callibri 20')
screen.mainloop()