import tkinter as tk
from tkinter import ttk
from app.addShiftWindow import AddShiftWindow


class ShiftWindow(tk.Toplevel):

    def __init__(self, master, db, name, id):
        super().__init__(master=master)
        self.db = db
        self.name = name
        self.id = id
        self.title('Employee app - shift screen')
        self.geometry('1920x1080+0+0')
        self.config(bg='#2c3e50')
        self.state('zoomed')

        self.mainFrame = tk.Frame(self, bg='#2c3e50')
        self.mainFrame.pack(side=tk.TOP, fill=tk.X)

        self.btnFrame = tk.Frame(self.mainFrame, bg='#2c3e50')
        self.btnFrame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky='w')
        self.btnAddShift = tk.Button(self.btnFrame, command=self.addShift, text='Add shift', width=20,
                                       font=('Calibri', 16, 'bold'),
                                       fg='white',
                                       bg='#579fea', bd=0).grid(row=0, column=3, padx=80)
        self.btnBack = tk.Button(self.btnFrame, command=self.back, text='Back', width=20,
                                     font=('Calibri', 16, 'bold'),
                                     fg='white',
                                     bg='#579fea', bd=0).grid(row=1, column=3, padx=80)

        self.lblNametxt = tk.Label(self.btnFrame, text='Employee:', font=('Calibri', 35), bg='#2c3e50', fg='white').grid(
            row=0, column=0, padx=10)
        self.lblName = tk.Label(self.btnFrame, textvariable=self.name, font=('Calibri', 35), bg='#2c3e50', fg='white').grid(
            row=0, column=1, padx=10)
        self.lblSumTxt = tk.Label(self.btnFrame, text='To pay: ', font=('Calibri', 35), bg='#2c3e50', fg='white').grid(
            row=1, column=0, padx=10)
        self.lblSum = tk.Label(self.btnFrame, text='0', font=('Calibri', 35), bg='#2c3e50', fg='white')
        self.lblSum.grid(row=1, column=1, padx=10)
        #self.lblSumZl = tk.Label(self.btnFrame, text='zł', font=('Calibri', 35), bg='#2c3e50', fg='white').grid(
            #row=1, column=2)
        #delete i edit shift? TODO

        # Table Frame
        self.treeFrame = tk.Frame(self, bg='#ecf0f1')
        self.treeFrame.place(x=0, y=150, width=1980, height=850)
        self.style = ttk.Style()
        self.style.configure('mystyle.Treeview', font=('Calibri', 18), rowheight=50)  # Modify the font of the body
        self.style.configure('mystyle.Treeview.Heading', font=('Calibri', 18))  # Modify the font of the headings
        self.treeView = ttk.Treeview(self.treeFrame, columns=(1, 2, 3, 4 , 5), style='mystyle.Treeview')
        self.treeView.heading('1', text='ID')
        self.treeView.column('1', width=5)
        self.treeView.heading('2', text='Date')
        self.treeView.heading('3', text='Due')
        self.treeView.heading('4', text='Hours')
        self.treeView.heading('5', text='Minutes')

        self.treeView['show'] = 'headings'
        #self.treeView.bind('<ButtonRelease-1>', self.getData)
        self.treeView.pack(fill=tk.BOTH, expand=True)
        self.displayAll()

    def displayAll(self):
        self.updateSum()
        self.treeView.delete(*self.treeView.get_children())
        for row in self.db.fetchShifts(self.id.get()):
            self.treeView.insert('', tk.END, values=row)

    def addShift(self):
        addShiftWindow = AddShiftWindow(self, self.db, self.id)
        addShiftWindow.grab_set()
        self.displayAll()

    def updateSum(self):
        row = self.db.fetchSumShifts(self.id.get())
        self.lblSum.config(text=row[0][0])

    def back(self):
        self.destroy()
