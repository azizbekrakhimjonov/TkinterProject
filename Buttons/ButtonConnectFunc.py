# from tkinter import Button, Tk
#
# root = Tk()
# def OnPressBtn():
#     print('On Click button')
#
# button = Button(root, text='Click me', command=OnPressBtn)
# button.pack()
#
# root.mainloop()


from tkinter import Tk, Button

root = Tk()
root.geometry('300x400')
root.config(bg='green')

def f():
    root.config(bg='red')

btn = Button(root, text='Next Color', command=f)
btn.pack()

root.mainloop()