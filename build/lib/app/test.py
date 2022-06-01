from empWindow import EmpWindow
from app.db import Database

if __name__ == '__main__':
    db = Database("app/Employee.db")
    empwin = EmpWindow(db)
    empwin.run()


