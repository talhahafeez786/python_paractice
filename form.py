from cProfile import label
from cgitb import text
import imp
from importlib.metadata import entry_points
from logging import root
from sqlite3 import Row
from tabnanny import check
from tkinter import *
from tkinter import font
from tkinter.tix import COLUMN
from tokenize import Name
from unicodedata import name
root = Tk()
root.geometry("500x300")
Label(root, text='Registration Form', font="ar 15 bold").grid(row=0,column=0)

Name = Label(root, text="Name")
Phone = Label(root, text="Phone")
Gender = Label(root, text="Gender")
Emergency = Label(root, text="Emergency")
Paymentmood = Label(root, text="Payment Mood")

Name.grid(row=1,column=2)
Phone.grid(row=2,column=2)
Gender.grid(row=3,column=2)
Emergency.grid(row=4,column=2)
Paymentmood.grid(row=5,column=2)

Namevalue = StringVar
Phonevalue = StringVar
Gendervalue = StringVar
Emergencyvalue = StringVar
Paymentmoodvalue = StringVar
checkvalue = IntVar

Nameentry = Entry(root, textvariable=Namevalue)
Phoneentry = Entry(root, textvariable=Phonevalue)
Genderentry = Entry(root, textvariable=Gendervalue)
Emergencyentry = Entry(root, textvariable=Emergencyvalue)
Paymentmoodentry = Entry(root, textvariable=Paymentmoodvalue)

Nameentry.grid(row=1,column=3)
Phoneentry.grid(row=2,column=3)
Genderentry.grid(row=3,column=3)
Emergencyentry.grid(row=4,column=3)
Paymentmoodentry.grid(row=5,column=3)

Checkbtn = Checkbutton(text="remember me", variable=checkvalue)
Checkbtn.grid(row=6, column=3)

Button(text="submit").grid(row=7, column=3)



root.mainloop()