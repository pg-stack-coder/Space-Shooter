import tkinter as tk
from tkinter import ttk
screen=tk.Tk( )
screen.geometry('600x600')
screen.title('challenge 1')

frame=ttk.Frame(screen)
button=tk.Button(frame,text='button1')
button2=tk.Button(frame,text='button2')
button5=tk.Button(frame,text='button5')
slider=ttk.Scale(frame,orient='vertical')
slider2=ttk.Scale(frame,orient='vertical')
check_frame=ttk.Frame(frame)
check=ttk.Checkbutton(check_frame,text='check 1')
check2=ttk.Checkbutton(check_frame,text='check 2')
entry=ttk.Entry(frame)


frame2=ttk.Frame(screen,)
subframe=ttk.Frame(frame2)
subframe2=ttk.Frame(frame2)
label=tk.Label(subframe,text='Label 1',bg='red')
labe2=tk.Label(subframe2,text='Label 2',bg='blue')
button3=tk.Button(subframe,text='button3')
button4=tk.Button(subframe2,text='button4')
frame.place(x=0,y=0,relwidth=0.3,relheight=1)
frame2.place(relx=0.3,y=0,relwidth=0.7,relheight=1)

#grid
frame.columnconfigure((0,1,2),weight=1,uniform='a')
frame.rowconfigure((0,1,2,3,4),weight=1,uniform='a')
button.grid(column=0,row=0,columnspan=2,sticky='news',padx=10)
button2.grid(column=2,row=0,sticky='news')
button5.grid(column=0,row=1,columnspan=3,sticky='news',pady=10)
slider.grid(column=0,row=2,rowspan=2,sticky='news' )
slider2.grid(column=2,row=2,rowspan=2,sticky='news')
check_frame.grid(row=4,column=0,columnspan=3,sticky='news')
check.pack(side='left',expand=True,fill='both',padx=20)
check2.pack(side='left',expand=True,fill="both")
entry.place(relx=0.5,rely=0.95,anchor='center')

#right frame
subframe.pack(side='left',expand=True,fill='both',padx=10,pady=10)
subframe2.pack(side='left',expand=True,fill='both',pady=10)
label.pack(expand=True,fill='both')
button3.pack(expand=True,fill='both',pady=10)
labe2.pack(expand=True,fill='both')
button4.pack(expand=True,fill='both',pady=10)




# label=tk.Label(frame,text='Label 1',bg='red')
# labe2=tk.Label(frame2,text='Label 2',bg='blue')
# label.pack(fill='both',expand=True)
# labe2.pack(fill='both',expand=True)

screen.mainloop()