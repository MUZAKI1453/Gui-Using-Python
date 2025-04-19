# import library tkinter
from tkinter import *

root = Tk() # membuat window utama
root.title("make Icons") # judul dari widget / layar utama

# membuat ikon pada widget, ekstensi dari file ikon harus .ico
root.iconbitmap(r"D:\Python\Gambar\icon.ico")

root.mainloop() # menjalankan aplikasi (loop utama gui)