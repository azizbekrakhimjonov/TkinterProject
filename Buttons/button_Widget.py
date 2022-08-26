from tkinter import Button, Tk

root = Tk()
root.geometry('500x400')
button = Button(root, text='Click me', bg='green', font=('consolas', 24), width=20)
button.pack()

root.mainloop()