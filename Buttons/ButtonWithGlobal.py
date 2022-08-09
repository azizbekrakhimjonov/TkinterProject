from tkinter import *
root = Tk()

count = 0

def OnClickCount():
    global count
    count += 1
    print(count)

btn = Button(root, text='Click', command=OnClickCount)
btn.pack()

root.mainloop()
