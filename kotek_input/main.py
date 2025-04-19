# import library
from tkinter import *

root = Tk()

# ini adalah input box
e = Entry(root, width=20, borderwidth=5)
e.pack()
# e.insert itu untuk menambahkan tulisan didalam input box yang bersifat default value
e.insert(0, "input here")

#def ButtonClick():
    # e.get -> untuk mendapatkan kembali apa yang kita input pada box input
    #MyLabel = Label(root, text=e.get(), padx=10, pady=10)
    #MyLabel.pack()

#def ButtonClick():
    #MyLabel = Label(root, text="Hello " + e.get())
    #MyLabel.pack()

# atau bisa juga seprti ini
def ButtonClick():
    Hello = "Hello " + e.get()
    MyLabel = Label(root, text=Hello)
    MyLabel.pack()

MyButton = Button(root, text="Enter Your Name", command=ButtonClick, fg="blue", bg="white", padx=5, pady=5)
MyButton.pack()

# ini looping program gui
root.mainloop()