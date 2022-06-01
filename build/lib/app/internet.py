import tkinter as tk
from tkinter import ttk

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Toplevel Window')



        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(expand=True)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Main Window')

        self.name = tk.StringVar()
        self.birthdate = tk.StringVar()
        self.phone = tk.StringVar()
        self.banknum = tk.StringVar()
        self.hourlyrate = tk.DoubleVar()
        self.topay = tk.DoubleVar()

        self.mainFrame = tk.Frame(self, bg="#535c68")
        self.mainFrame.pack(side=tk.TOP, fill=tk.X)

        self.lblName = tk.Label(self.mainFrame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
        self.lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txtName = tk.Entry(self.mainFrame, textvariable=self.name, font=("Calibri", 16), width=30)
        self.txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # place a button on the root window
        ttk.Button(self,
                text='Open a window',
                command=self.open_window).pack(expand=True)

    def open_window(self):
        window = Window(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()