from tkinter import Tk, Button

root = Tk()

count = 0
def f():
    global count
    count += 1
    print(count)
    btn.config(text = count)

btn = Button(root, text='Join', command=f)
btn.pack()

root.mainloop()