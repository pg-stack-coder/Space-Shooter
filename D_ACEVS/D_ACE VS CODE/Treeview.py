import tkinter as tk
from tkinter import ttk
from random import choice
screen=tk.Tk()
screen.geometry('600x600')
screen.title('challenge 1')
list1=['ruthless','kind','lame','funny','mundane']
list2=['newton','tiger','taylor','homes','smith']
def item_select():
    for i in tree.selection():
        print(tree.item(i)['values'])
def delete_item(_):
    for i in tree.selection():
        tree.delete(i)
tree=ttk.Treeview(screen,columns=('first','second',"third"),show='headings')
tree.heading('first',text='First')
tree.heading('second',text='Second')
tree.heading('third',text='Third')
tree.pack()
for i in range(100):
    first=choice(list1)
    second=choice(list2)
    third=f"{first}{second}@gmail.com"
    data=(first,second,third)
    tree.insert(parent='',index=0,value=data)
tree.bind("<<TreeviewSelect>>",lambda event:item_select())
tree.bind('<Delete>',delete_item)
screen.mainloop()





