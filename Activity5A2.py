from tkinter import *
from tkinter.ttk import *

master = Tk()
master.title('Hello Python')
master.geometry('400x300')
master.resizable(False, False)

var = StringVar()
var.set("male")
var1 = BooleanVar()
var2 = BooleanVar()

Radiobutton(master, text="Male", variable=var, value="male").grid(row=0, column=0, padx=10, pady=10)
Radiobutton(master, text="Female", variable=var, value="female").grid(row=0, column=1, padx=10, pady=10)

# center the radio buttons horizontally
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)

Checkbutton(master, text="Cricket", variable=var1).grid(row=1, column=0, padx=10, pady=10)
Checkbutton(master, text="Tennis", variable=var2).grid(row=1, column=1, padx=10, pady=10)

combo = Combobox(master, values=["One", "Two", "Three", "Four"])
combo.grid(row=2, column=0, padx=10, pady=10)
combo.current(0)

listbox = Listbox(master)
listbox.grid(row=2, column=1, padx=10, pady=10)
listbox.insert(END, "First")
listbox.insert(END, "Two")
listbox.insert(END, "Three")
listbox.insert(END, "Four")

mainloop()


master = Tk()
master.title('Hello Python')
master.geometry('400x300')
master.resizable(False, False)

var = StringVar()
var.set("male")
var1 = BooleanVar()
var2 = BooleanVar()

Radiobutton(master, text="Male", variable=var, value="male").grid(row=0, column=0, padx=10, pady=10)
Radiobutton(master, text="Female", variable=var, value="female").grid(row=0, column=1, padx=10, pady=10)

# center the radio buttons horizontally
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)

Checkbutton(master, text="Cricket", variable=var1).grid(row=1, column=0, padx=10, pady=10)
Checkbutton(master, text="Tennis", variable=var2).grid(row=1, column=1, padx=10, pady=10)

combo = Combobox(master, values=["One", "Two", "Three", "Four"])
combo.grid(row=2, column=0, padx=10, pady=10)
combo.current(0)

listbox = Listbox(master)
listbox.grid(row=2, column=1, padx=10, pady=10)
listbox.insert(END, "First")
listbox.insert(END, "Two")
listbox.insert(END, "Three")
listbox.insert(END, "Four")

mainloop()
