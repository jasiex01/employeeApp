import tkinter as tk
from tkinter import ttk
from app.loginWindow import LoginWindow
from app.shiftWindow import ShiftWindow
from tkinter import messagebox


class EmpWindow(tk.Tk):
        def __init__(self, db):
                super().__init__()
                self.db = db

                self.name = tk.StringVar()
                self.id = tk.IntVar(value=0)

                self.title('Employee app - main')
                self.geometry('1920x1080+0+0')
                self.config(bg='#2c3e50')
                self.state('zoomed')

                self.mainFrame = tk.Frame(self, bg='#2c3e50')
                self.mainFrame.pack(side=tk.TOP, fill=tk.X)


                self.btnFrame = tk.Frame(self.mainFrame, bg='#2c3e50')
                self.btnFrame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky='w')
                self.btnShowShifts = tk.Button(self.btnFrame, command=self.showShifts, text='Show employee shifts', width=20,
                                               font=('Calibri', 16, 'bold'),
                                               fg='white',
                                               bg='#579fea', bd=0).grid(row=0, column=0, padx=10)
                self.btnMng = tk.Button(self.btnFrame, command=self.enterMngMode, text='Manager login', width=15,
                                        font=('Calibri', 16, 'bold'),
                                        fg='white', bg='#579fea',
                                        bd=0).grid(row=0, column=1, padx=10)
                self.btnRefresh = tk.Button(self.btnFrame, command=self.displayAll, text='Refresh', width=15,
                                        font=('Calibri', 16, 'bold'),
                                        fg='white', bg='#579fea',
                                        bd=0).grid(row=0, column=2, padx=10)

                # Table Frame
                self.treeFrame = tk.Frame(self, bg='#ecf0f1')
                self.treeFrame.place(x=0, y=65, width=1980, height=935)
                self.style = ttk.Style()
                self.style.configure('mystyle.Treeview', font=('Calibri', 18), rowheight=50)  # Modify the font of the body
                self.style.configure('mystyle.Treeview.Heading', font=('Calibri', 18))  # Modify the font of the headings
                self.treeView = ttk.Treeview(self.treeFrame, columns=(1, 2), style='mystyle.Treeview')
                self.treeView.heading('1', text='ID')
                self.treeView.column('1', width=5)
                self.treeView.heading('2', text='Name')
                self.treeView.column('2', width=900)


                self.treeView['show'] = 'headings'
                self.treeView.bind('<ButtonRelease-1>', self.getData)
                self.treeView.pack(fill=tk.BOTH, expand=True)

        def displayAll(self):
                self.treeView.delete(*self.treeView.get_children())
                for row in self.db.fetchEmployees():
                        self.treeView.insert('', tk.END, values=row)

        def enterMngMode(self):
                #top level with login (if login correct open mng window)
                loginWindow = LoginWindow(self, self.db)
                loginWindow.grab_set()

        def showShifts(self):
                # toplevel window with employee shifts
                if self.id.get() != 0:
                        shiftWindow = ShiftWindow(self, self.db, self.name, self.id)
                        shiftWindow.grab_set()
                else:
                        messagebox.showerror('Error', 'Choose an employee')

        def getData(self, event):
                selected_row = self.treeView.focus()
                data = self.treeView.item(selected_row)
                global row
                row = data['values']
                self.id.set(row[0])
                self.name.set(row[1])

        def run(self):
                self.displayAll()
                self.mainloop()

        #root.mainloop()
