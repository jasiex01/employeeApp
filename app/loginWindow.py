import tkinter as tk
from tkinter import messagebox
from app.mngWindow import MngWindow

class LoginWindow(tk.Toplevel):

    def __init__(self, master, db):
        super().__init__(master=master)
        self.db = db

        self.title("Employee app - manager login")
        self.geometry('400x150')
        self.password = tk.StringVar()

        self.topFrame = tk.Frame(self, bg='#2c3e50')
        self.topFrame.pack(side=tk.TOP, fill=tk.X)
        self.bottomFrame = tk.Frame(self, bg='#2c3e50')
        self.bottomFrame.pack(side=tk.BOTTOM, fill=tk.X)

        self.passwordLabel = tk.Label(self.topFrame, text="Password", font=('Calibri', 16), bg='#2c3e50', fg='white'
                                      ).grid(row=0, column=0)
        self.passwordEntry = tk.Entry(self.topFrame, textvariable=self.password, show='*',
                                      font=('Calibri', 16), width=30).grid(row=0, column=1, pady=20)

        self.loginButton = tk.Button(self.bottomFrame, text="Login", command=self.validatePassword,
                                     font=('Calibri', 16, 'bold'), fg='white', bg='#579fea', bd=0).grid(row=0, column=0, pady=20, padx=170)


    def validatePassword(self):
        if self.password.get() == '1234':  # hard coded password - todo
            self.destroy()
            mngwin = MngWindow(self.db)
            mngwin.displayAll()
            mngwin.grab_set()

        else:
            messagebox.showerror("Error", "Wrong password")
