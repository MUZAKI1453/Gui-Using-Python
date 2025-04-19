# import library Tkinter
from tkinter import *

root = Tk()

MyLabel1 = Label(root, text="Hello World !!").grid(row=0, column=0)
MyLabel2 = Label(root, text="My Name is Muhamad Arif Muzaki").grid(row=1, column=2)
Label_kosong = Label(root, text="                                       ").grid(row=1, column=0)

# grid untuk mengatur tata letak
#MyLabel1.grid(row=0, column=0)
#MyLabel2.grid(row=1, column=3)
#Label_kosong.grid(row=1, column=2)

# looping program
root.mainloop()