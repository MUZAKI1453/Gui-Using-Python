# import library tkinter
from tkinter import *

root = Tk()
# judul widget
root.title("Simple Calculator")

# input box
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonClick(number):
    #e.delete(0, END)
    current = e.get()

    # ini fungsi untuk menghapus hasil inputan sebelumnya, karena sebelumnya ketika input 2 kali inputan sebelunya akan ikut
    e.delete(0, END)

    e.insert(0, str(current) + str(number))
    return

# menghapus angka yg dimasukan
def button_clear():
    e.delete(0, END)

# button add untuk angka pertama
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

# button add untuk angka ke dua
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "pengurangan":
        e.insert(0, f_num - int(second_number))

    if math == "perkalian":
        e.insert(0, f_num * int(second_number))

    if math == "pembagian":
        e.insert(0, f_num / int(second_number))


# button pengurangan
def button_pengurangan():
    first_number = e.get()
    global f_num
    global math
    math = "pengurangan"
    f_num = int(first_number)
    e.delete(0, END)

# button perkalian
def button_perkalian():
    first_number = e.get()
    global f_num
    global math
    math = "perkalian"
    f_num = int(first_number)
    e.delete(0, END)

# button pembagian
def button_pembagian():
    first_number = e.get()
    global f_num
    global math
    math = "pembagian"
    f_num = int(first_number)
    e.delete(0, END)


# tombol
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))
button_tambah = Button(root, text="+", padx=39, pady=20, command= button_add)
button_samaDengan = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_hapus = Button(root, text="hapus", padx=79, pady=20, command= button_clear)

button_pengurangan = Button(root, text="-", padx=41, pady=20, command= button_pengurangan)
button_perkalian = Button(root, text="x", padx=40, pady=20, command= button_perkalian)
button_pembagian = Button(root, text="/", padx=40, pady=20, command= button_pembagian)

# put button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_hapus.grid(row=4, column=1, columnspan=2)
button_tambah.grid(row=5, column=0)
button_samaDengan.grid(row=5, column=1, columnspan=2)

button_pengurangan.grid(row=6, column=0)
button_perkalian.grid(row=6, column=1)
button_pembagian.grid(row=6, column=2)


root.mainloop()