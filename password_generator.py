import random
import pyperclip
from tkinter import *
from tkinter.ttk import *


def low():
    entry.delete(0, END)

    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for _ in range(length):
            password += random.choice(lower)
        return password

    elif var.get() == 0:
        for _ in range(length):
            password += random.choice(upper)
        return password

    elif var.get() == 3:
        for _ in range(length):
            password += random.choice(digits)
        return password
    else:
        print("Please choose an option")


def generate():
    password1 = low()
    entry.delete(0, END)
    entry.insert(END, password1)


def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)


root = Tk()
var = IntVar()
var1 = IntVar()


root.title("Random Password Generator")


Random_password = Label(root, text="Password")
Random_password.grid(row=0, pady=10)
entry = Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2, padx=10, pady=10)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3, padx=10, pady=10)


c_label = Label(root, text="Length")
c_label.grid(row=1, pady=5)


radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='W', padx=5, pady=5)
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='W', padx=5, pady=5)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='W', padx=5, pady=5)


combo = Combobox(root, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.grid(column=1, row=1, padx=10, pady=5)


root.mainloop()
