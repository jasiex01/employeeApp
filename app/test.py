from app.empWindow import EmpWindow
from app.db import Database

db = Database('C:/Users/herna/PycharmProjects/employeeApp/app/Employee.db')
empwin = EmpWindow(db)
empwin.run()

#if __name__ == '__main__':



