import tkinter as tk
from tkinter import ttk
screen=tk.Tk()
screen.geometry('600x600')
screen.title('challenge 1')
screen.config(bg='light blue')
canvas=tk.Canvas(screen,bg='white')
canvas.pack()
brush=2

def draw(event):
    x= event.x
    y= event.y
    canvas.create_oval(x-brush/2,y-brush/2,x+brush/2,y+brush/2,fill='black')
def adjust_brush(event):
    global brush
    if event.delta>0:
        brush+=4
    else:
        brush-=4
    brush=max(0,min(brush,50))
canvas.bind('<Alt-Motion>',draw)
canvas.bind('<MouseWheel>',adjust_brush)
screen.mainloop()