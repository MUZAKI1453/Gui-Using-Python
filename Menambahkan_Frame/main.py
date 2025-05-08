# menambahkan frame atau bingkai ke widget

from tkinter import *
from PIL import ImageTk,Image

root = Tk()

# ini adalah title pada widget
root.title("Menambahkan Frame ke Widget")

# ini adalah icon pada widget
root.iconbitmap(r"D:\Python\Gambar\icon.ico")

# membuat frame
frame = LabelFrame(root, text="ini adalah frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

# membuat button
b = Button(frame, text="jangan klik ini !")
b2 = Button(frame, text="yang ini aja !")
b.grid(row=0, column=0)
b2.grid(row=4, column=1)

root.mainloop()