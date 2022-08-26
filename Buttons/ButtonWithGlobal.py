from tkinter import *

root = Tk()

count = 0


def f():
    global count
    count += 1
    print(count)
    btn.config(text=count)
    if count == 20:
        btn.config(state=DISABLED)
    else:
        btn.config(state=NORMAL)


btn = Button(root, text='Join', command=f)
btn.pack()

root.mainloop()
