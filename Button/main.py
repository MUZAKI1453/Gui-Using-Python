# import library Tkinter
from tkinter import *

root = Tk()

# buton
#MyButton = Button(root, text="click me")

# ini contoh button yang disabled / atau tidak bisa dipencet
# MyButton = Button(root, text="click me", state=DISABLED)

# ini melebarkan ukuran button, x = vertikal dan y = horizontal
MyButton = Button(root, text="click me", padx = 50, pady = 50)

# menampilkan gui ke layar
MyButton.pack()

# looping program gui
root.mainloop()