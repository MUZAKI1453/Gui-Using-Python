# import library
from tkinter import *

root = Tk()

# fungsi, bila button di klik akan menampilkan pesan widget di layar
def ButtonClick():
    MyLabel = Label(root, text="look i cliked button !", fg="blue")
    MyLabel.pack()

# menampilkan button pada widget, dan sudah menggunakan fungsi ButtonClick diatas
#MyButton = Button(root, text="click me", command=ButtonClick)

# mungubah warna button, dengan fg="warnanya"
# memberikan warna background dengan bg="warnanya"
MyButton = Button(root, text="click me", command=ButtonClick, fg="red", bg="yellow")

# menampilkan gui ke layar
MyButton.pack()

# looping program gui
root.mainloop()