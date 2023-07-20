from tkinter import *

root = Tk()
root.title('Address Entry Form')
root.geometry('500x300')
root.resizable(False, False)

F_name = StringVar()
L_name = StringVar()
Address_line1 = StringVar()
Address_line2 = StringVar()
city = StringVar()
state = StringVar()
code = IntVar()
country = StringVar()

Label(root, text='First Name:').grid(row=0, column=0)
Label(root, text='Last Name:').grid(row=1, column=0)
Label(root, text='Address Line 1:').grid(row=2, column=0)
Label(root, text='Address Line 2:').grid(row=3, column=0)
Label(root, text='City:').grid(row=4, column=0)
Label(root, text='State/Province:').grid(row=5, column=0)
Label(root, text='Postal Code:').grid(row=6, column=0)
Label(root, text='Country:').grid(row=7, column=0)

Entry(root, textvariable=F_name, width=60).grid(row=0, column=3)
Entry(root, textvariable=L_name, width=60).grid(row=1, column=3)
Entry(root, textvariable=Address_line1, width=60).grid(row=2, column=3)
Entry(root, textvariable=Address_line2, width=60).grid(row=3, column=3)
Entry(root, textvariable=city, width=60).grid(row=4, column=3)
Entry(root, textvariable=state, width=60).grid(row=5, column=3)
Entry(root, textvariable=code, width=60).grid(row=6, column=3)
Entry(root, textvariable=country, width=60).grid(row=7, column=3)

def clear_form():
    F_name.set('')
    L_name.set('')
    Address_line1.set('')
    Address_line2.set('')
    city.set('')
    state.set('')
    code.set('')
    country.set('')

Button(root, text='Submit').grid(row=8, column=1, pady=10)
Button(root, text='Clear', command=clear_form).grid(row=8, column=0, pady=10, padx=10, sticky=E)

root.mainloop()

