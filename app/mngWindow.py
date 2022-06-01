import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MngWindow(tk.Toplevel):
    def __init__(self, db):
        super().__init__()
        self.db = db
        # root = Tk()
        self.title('Employee app - manager screen')
        self.geometry('1920x1080+0+0')
        self.config(bg='#2c3e50')
        self.state('zoomed')

        self.name = tk.StringVar()
        self.birthdate = tk.StringVar()
        self.phone = tk.StringVar()
        self.banknum = tk.StringVar()
        self.hourlyrate = tk.DoubleVar()
        self.topay = tk.DoubleVar()

        # Entries Frame
        self.mainFrame = tk.Frame(self, bg='#2c3e50')
        self.mainFrame.pack(side=tk.TOP, fill=tk.X)
        self.title = tk.Label(self.mainFrame, text='Specify employee details', font=('Calibri', 16, 'bold'),
                              bg='#2c3e50',
                              fg='white')
        self.title.grid(row=0, columnspan=2, padx=10, pady=20, sticky='w')

        self.lblName = tk.Label(self.mainFrame, text='Name', font=('Calibri', 16), bg='#2c3e50', fg='white')
        self.lblName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.txtName = tk.Entry(self.mainFrame, textvariable=self.name, font=('Calibri', 16), width=30)
        self.txtName.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.lblBirthdate = tk.Label(self.mainFrame, text='Date of birth', font=('Calibri', 16), bg='#2c3e50', fg='white')
        self.lblBirthdate.grid(row=1, column=2, padx=10, pady=10, sticky='w')
        self.txtBirthdate = tk.Entry(self.mainFrame, textvariable=self.birthdate, font=('Calibri', 16), width=30)
        self.txtBirthdate.grid(row=1, column=3, padx=10, pady=10, sticky='w')

        self.lblPhone = tk.Label(self.mainFrame, text='Phone', font=('Calibri', 16), bg='#2c3e50', fg='white')
        self.lblPhone.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.txtPhone = tk.Entry(self.mainFrame, textvariable=self.phone, font=('Calibri', 16), width=30)
        self.txtPhone.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        self.lblBanknum = tk.Label(self.mainFrame, text='Account number', font=('Calibri', 16), bg='#2c3e50', fg='white')
        self.lblBanknum.grid(row=2, column=2, padx=10, pady=10, sticky='w')
        self.txtBanknum = tk.Entry(self.mainFrame, textvariable=self.banknum, font=('Calibri', 16), width=30)
        self.txtBanknum.grid(row=2, column=3, padx=10, pady=10, sticky='w')

        self.lblHourlyrate = tk.Label(self.mainFrame, text='Hourly rate', font=('Calibri', 16), bg='#2c3e50', fg='white')
        self.lblHourlyrate.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.txtHourlyrate = tk.Entry(self.mainFrame, textvariable=self.hourlyrate, font=('Calibri', 16), width=30)
        self.txtHourlyrate.grid(row=3, column=1, padx=10, sticky='w')

        self.btnFrame = tk.Frame(self.mainFrame, bg='#2c3e50')
        self.btnFrame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky='w')
        self.btnAdd = tk.Button(self.btnFrame, command=self.add_employee, text='Add details', width=15,
                                font=('Calibri', 16, 'bold'),
                                fg='white',
                                bg='#579fea', bd=0).grid(row=0, column=0, padx=10)
        self.btnEdit = tk.Button(self.btnFrame, command=self.updateEmployee, text='Update details', width=15,
                                 font=('Calibri', 16, 'bold'),
                                 fg='white', bg='#579fea',
                                 bd=0).grid(row=0, column=1, padx=10)
        self.btnDelete = tk.Button(self.btnFrame, command=self.deleteEmployee, text='Delete details', width=15,
                                   font=('Calibri', 16, 'bold'),
                                   fg='white', bg='#579fea',
                                   bd=0).grid(row=0, column=2, padx=10)
        self.btnClear = tk.Button(self.btnFrame, command=self.clearAll, text='Clear details', width=15,
                                  font=('Calibri', 16, 'bold'),
                                  fg='white',
                                  bg='#579fea',
                                  bd=0).grid(row=0, column=3, padx=10)
        self.btnPayOut = tk.Button(self.btnFrame, command=self.payOut, text='Pay out all', width=15,
                                   font=('Calibri', 16, 'bold'),
                                   fg='white',
                                   bg='#579fea',
                                   bd=0).grid(row=0, column=4, padx=10)
        self.btnBack = tk.Button(self.btnFrame, command=self.back, text='Back', width=15,
                                   font=('Calibri', 16, 'bold'),
                                   fg='white',
                                   bg='#579fea',
                                   bd=0).grid(row=0, column=5, padx=10)

        # Table Frame
        self.treeFrame = tk.Frame(self, bg='#ecf0f1')
        self.treeFrame.place(x=0, y=300, width=1980, height=700)
        self.style = ttk.Style()
        self.style.configure('mystyle.Treeview', font=('Calibri', 18), rowheight=50)
        self.style.configure('mystyle.Treeview.Heading', font=('Calibri', 18))

        self.treeView = ttk.Treeview(self.treeFrame, columns=(1, 2, 3, 4, 5, 6, 7), style='mystyle.Treeview')
        self.treeView.heading('1', text='ID')
        self.treeView.column('1', width=5)
        self.treeView.heading('2', text='Name')
        self.treeView.heading('3', text='Date of birth')
        self.treeView.column('3', width=5)
        self.treeView.heading('4', text='Phone')
        self.treeView.column('4', width=10)
        self.treeView.heading('5', text='Account number')
        self.treeView.heading('6', text='Hourly rate')
        self.treeView.column('6', width=10)
        self.treeView.heading('7', text='To pay')

        self.treeView['show'] = 'headings'
        self.treeView.bind('<ButtonRelease-1>', self.getData)

        self.treeView.pack(fill=tk.BOTH, expand=True)

    def getData(self, event):
        selected_row = self.treeView.focus()
        data = self.treeView.item(selected_row)
        global row
        row = data['values']
        # print(row)
        self.name.set(row[1])
        self.birthdate.set(row[2])
        self.phone.set(row[3])
        self.banknum.set(row[4])
        self.hourlyrate.set(row[5])
        self.topay.set(row[6])

    def displayAll(self):
        self.treeView.delete(*self.treeView.get_children())
        for row in self.db.mngFetchEmployees():
            self.treeView.insert('', tk.END, values=row)

    def add_employee(self):
        if self.txtName.get() == '' or self.txtBirthdate.get() == '' or self.txtPhone.get() == '' or self.txtBanknum.get() == '' or self.txtHourlyrate.get() == '':
            messagebox.showerror('Input error', 'Please fill all fields')
            return
        self.db.insertEmployee(self.txtName.get(), self.txtBirthdate.get(), self.txtPhone.get(), self.txtBanknum.get(),
                               self.txtHourlyrate.get())
        # messagebox.showinfo("Success", "Record Inserted")
        self.clearAll()
        self.displayAll()

    def updateEmployee(self):
        if self.txtName.get() == '' or self.txtBirthdate.get() == '' or self.txtPhone.get() == '' or self.txtBanknum.get() == '' or self.txtHourlyrate.get() == '':
            messagebox.showerror('Input error', 'Please fill all fields')
            return
        self.db.updateEmployee(row[0], self.txtName.get(), self.txtBirthdate.get(), self.txtPhone.get(),
                               self.txtBanknum.get(), self.txtHourlyrate.get(), )
        # messagebox.showinfo("Success", "Record Update")
        self.clearAll()
        self.displayAll()

    def deleteEmployee(self):
        self.db.removeEmployee(row[0])
        self.clearAll()
        self.displayAll()

    def clearAll(self):
        self.name.set('')
        self.birthdate.set('')
        self.phone.set('')
        self.banknum.set('')
        self.hourlyrate.set('')

    def payOut(self):
        msgbox = tk.messagebox.askquestion('Pay out - delete all shifts', 'Are you sure?')
        if msgbox == 'yes':
                self.db.deleteAllShifts()
        self.clearAll()
        self.displayAll()

    def back(self):
        self.destroy()