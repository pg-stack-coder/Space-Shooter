import tkinter as tk
from tkinter import ttk
screen=tk.Tk( )
# screen.geometry('600x600')
screen.title('challenge 1')
h=600
w=600
a=screen.winfo_screenheight()/2-h/2
b=screen.winfo_screenwidth()/2-w/2
screen.geometry(f'{w}x{h}+{int(b)}+{int(a)}')
screen.minsize(width=600,height=600)


# frame=ttk.Frame(screen)
# button=tk.Button(frame,text='button1')
print(screen.winfo_screenheight(),screen.winfo_screenwidth())
# screen.attributes('-alpha',0.5)
# screen.attributes('-topmost',True)
# screen.bind('<Escape>',lambda event:screen.quit())
# # screen.attributes('-disable',True)
# # screen.attributes('-fullscreen',True)
# screen.overrideredirect(True)
# grip=ttk.Sizegrip(screen)
# grip.place(anchor='se',relx=1.0,rely=1.0)
screen.mainloop()