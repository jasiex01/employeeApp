import tkinter as tk
from tkinter import messagebox

class AddShiftWindow(tk.Toplevel):

    def __init__(self, master, db, idp):
        super().__init__(master=master)
        self.db = db
        self.idp = idp

        self.title("Add shift")
        self.geometry('400x150')
        self.config(bg='#2c3e50')

        self.hours = tk.StringVar(value='0')
        self.minutes = tk.StringVar()

        self.topFrame = tk.Frame(self, bg='#2c3e50')
        self.topFrame.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.bottomFrame = tk.Frame(self, bg='#2c3e50')
        self.bottomFrame.pack(side=tk.BOTTOM, fill=tk.X, expand=True)

        #self.mainFrame = tk.Frame(self, bg='#2c3e50')
        self.hoursLabel = tk.Label(self.topFrame, text="Hours", font=('Calibri', 16), bg='#2c3e50', fg='white').grid(row=0, column=0)
        self.hoursEntry = tk.Entry(self.topFrame, textvariable=self.hours, font=('Calibri', 16), width=30)
        self.hoursEntry.grid(row=0, column=1)
        self.minutesLabel = tk.Label(self.topFrame, text="Minutes", font=('Calibri', 16), bg='#2c3e50', fg='white').grid(row=1, column=0)
        self.minutesEntry = tk.Entry(self.topFrame, textvariable=self.minutes, font=('Calibri', 16), width=30).grid(row=1, column=1)

        self.addButton = tk.Button(self.bottomFrame, text="Add", command=self.addShift, font=('Calibri', 16, 'bold'), fg='white', bg='#579fea', bd=0).grid(row=0, column=0, padx=170)


    def addShift(self):
        if self.hours.get() != '' and self.minutes.get() != '':
            try:
                minutesWorked = int(self.hours.get()) * 60 + int(self.minutes.get())
                self.db.insertShift(minutesWorked, self.idp.get())
                self.master.displayAll()
                self.destroy()
            except ValueError:
                messagebox.showerror("Error", "Fill all fields correctly")

        else:
            messagebox.showerror("Error", "Fill all fields")
