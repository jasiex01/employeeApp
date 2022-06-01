from empWindow import EmpWindow
from db import Database

if __name__ == '__main__':
    db = Database('C:/Users/herna/PycharmProjects/employeeApp/app/Employee.db')
    empwin = EmpWindow(db)
    empwin.run()


