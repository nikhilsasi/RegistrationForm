from tkinter import *
from tkinter import messagebox
import tkinter.ttk
import tkinter.font as tkFont
import database as db

class MainClass:
    a = 3
    global w
    w = 3

    @staticmethod
    def validatelogin():
        # verify logins
        db.ConnectDB()

    @staticmethod
    def newloginform():
        messagebox.showerror(title=None, message=None)

    def __init__(self):
        global testing


if __name__ == '__main__':
    global mainwindow
    mainwindow = Tk()

    mainwindow.geometry('800x400')

    Label(mainwindow, text="New User").grid(row=0, column=1, padx=10, pady=10)

    vartype = StringVar()

    Label(mainwindow, text="First Name").grid(row=1, column=0, padx=10, pady=10)
    Entry(mainwindow, textvariable=vartype, width=40).grid(row=1, column=1)
    Label(mainwindow, text="Middle Name").grid(row=2, column=0, padx=10, pady=10)
    Entry(mainwindow, textvariable=vartype, width=40).grid(row=2, column=1)
    Label(mainwindow, text="Last Name").grid(row=3, column=0, padx=10, pady=10)
    Entry(mainwindow, textvariable=vartype, width=40).grid(row=3, column=1)
    Label(mainwindow, text="Course").grid(row=4, column=0, padx=10, pady=10)
    Entry(mainwindow, textvariable=vartype, width=40).grid(row=4, column=1)
    Label(mainwindow, text="Gender").grid(row=5, column=0, padx=10, pady=10)
    Entry(mainwindow, textvariable=vartype, width=40).grid(row=5, column=1)
    Label(mainwindow, text="Phone no.").grid(row=6, column=0, padx=10, pady=10)
    Entry(mainwindow, textvariable=vartype, width=40).grid(row=6, column=1)
    Label(mainwindow, text="Address").grid(row=7, column=0, padx=10, pady=10)
    Entry(mainwindow, textvariable=vartype, width=40).grid(row=7, column=1)

    Button(mainwindow, text='Sign Up', command=MainClass.newloginform).place(relx=0.15, rely=0.85)
    Button(mainwindow, text='Reset', command=MainClass.validatelogin).place(relx=0.3, rely=0.85)

    tkinter.ttk.Separator(mainwindow, orient=VERTICAL).grid(column=3, row=1, padx=50, rowspan=20, sticky='ns')

    Label(mainwindow, text="Username").grid(row=1, column=4, padx=2, pady=10)
    Entry(mainwindow, textvariable=vartype, width=35).grid(row=1, column=5)

    Label(mainwindow, text="Password").grid(row=2, column=4)
    Entry(mainwindow, textvariable=vartype, show="*", width=35).grid(row=2, column=5)

    lbl = Label(mainwindow, text=r"Forgot Password...?", fg="blue", cursor="hand2")
    f = tkFont.Font(lbl, lbl.cget("font"))
    f.configure(underline=True)
    lbl.configure(font=f)

    lbl.place(relx=0.75, rely=0.30)
    Button(mainwindow, text='Sign In', command=MainClass.validatelogin).place(relx=0.85, rely=0.35)

    mainwindow.mainloop()
