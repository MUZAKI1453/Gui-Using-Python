# import library tkinter
from tkinter import *

root = Tk() # membuat window utama
root.title("make exit Button") # judul dari widget / layar utama

# membuat ikon pada widget, ekstensi dari file ikon harus .ico
root.iconbitmap(r"D:\Python\Gambar\icon.ico")


# membuat button quit
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop() # menjalankan aplikasi (loop utama gui)