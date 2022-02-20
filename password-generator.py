# Python program to generate random password using Tkinter module
from cgitb import text
from doctest import master
import random
# import pyperclip
import pyperclip
from tkinter import *
from tkinter.ttk import *
from tkinter import font
import tkinter as tk

# Function for calculation of password
def low():
	entry.delete(0, END)

	# Get the length of password
	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""

	# if strength selected is low
	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	# if strength selected is medium
	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	# if strength selected is strong
	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")

# Function for generation of password
def generate():
	password1 = low()
	entry.insert(10, password1)


# Function for copying password to clipboard
def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)


# Main Function

# create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

# Title of your GUI window
root.title("Random Password Generator")
root.geometry("570x110")

# create label and entry to show
# password generated
Random_password = Label(root, text="Password:", font=("none",11))
Random_password.grid(row=1)
entry = Entry(root, font=("none", 11))
entry.grid(row=1, column=1, padx=10)

# create label for length of password
c_label = Label(root, text="Length:", font=("none", 11))
c_label.grid(row=11)

# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
copy_button = tk.Button(root, text="Copy", command=copy1, font=("none", 11))
copy_button.grid(row=11, column=2, padx=5)
generate_button = tk.Button(root, text="Generate", command=generate, font=("none", 11))
generate_button.grid(row=11, column=3, padx=5)

# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_low = tk.Radiobutton(root, text="Low", font=("none",11), variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E', padx=5)
radio_middle = tk.Radiobutton(root, text="Medium", font=("none",11), variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E', padx=5)
radio_strong = tk.Radiobutton(root, text="Strong",  font=("none",11), variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E', padx=5)
combo = Combobox(root, textvariable=var1, font=("none", 11))

# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=11)

# start the GUI
root.mainloop()
