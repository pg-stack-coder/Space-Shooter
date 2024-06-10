import tkinter as tk
from tkinter import ttk
screen=tk.Tk( )
screen.geometry('600x600')
screen.title('challenge 1')
frame=ttk.Frame(screen,)
label=tk.Label(frame,text='Label 1',bg='red')
labe2=tk.Label(frame,text='Label 2',bg='blue')
labe3=tk.Label(screen,text='Label 3',bg='green')





label.pack(side='left',fill='both',expand=True )
labe2.pack(side='left',fill='both',expand=True)
frame.pack(fill='both',expand=True)

labe3.pack(side='top',fill='both',expand=True)

frame2=ttk.Frame(screen)
button=tk.Button(frame2,text='button1')
button2=tk.Button(frame2,text='button2')
labe4=tk.Label(frame2,text='Label 4',bg='white')
labe4.pack(side='left',fill='both',expand=True )
button.pack(side='left',fill='both',expand=True)
button2.pack(side='left',fill='both',expand=True)
frame2.pack(padx=10,pady=10,fill='both',expand=True)

frame3=ttk.Frame(frame2)
button3=tk.Button(frame3,text='button3')
button4=tk.Button(frame3,text='button4')
button5=tk.Button(frame3,text='button5')
button3.pack(side='top',fill='both',expand=True)
button4.pack(side='top',fill='both',expand=True)
button5.pack(side='top',fill='both',expand=True)
frame3.pack(side='left',fill='both',expand=True)



screen.mainloop()
