from tkinter import *

master = Tk()

invoice_no = StringVar()
total_price = DoubleVar()
cash = DoubleVar()

Label(master, text='Invoice No: ').grid (row=0, column=0)
Label(master, text='Total Price: ').grid(row=1, column=0)
Label(master, text='Cash: ').grid(row=2, column=0)

Entry(master, textvariable=invoice_no).grid(row=0, column=3)
Entry(master, textvariable=total_price).grid(row=1, column=3)
Entry(master, textvariable=cash).grid(row=2, column=3)

Button(master, text='Submit').grid(row=6, columnspan=4)

mainloop()