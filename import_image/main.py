# import library tkinter
from tkinter import *

# import pil / python image library
# cara nya dengan jalankan perintah pip install pillow pd terminal
from PIL import ImageTk, Image

root = Tk() # membuat window utama
root.title("make exit Button") # judul dari widget / layar utama

# membuat ikon pada widget, ekstensi dari file ikon harus .ico
root.iconbitmap(r"D:\Python\Gambar\icon.ico")

# menampilkan image
myImage = ImageTk.PhotoImage(Image.open(r"D:\Python\Gambar\timnas.jpeg"))
myLabel = Label(image = myImage)
myLabel.pack()


# membuat button quit
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop() # menjalankan aplikasi (loop utama gui)