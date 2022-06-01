import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            birthdate text,
            phone text,
            banknum text,
            hourlyrate REAL 
        )
        """
        self.cur.execute(sql)
        sql = """
        CREATE TABLE IF NOT EXISTS shifts(
            ids Integer Primary Key,
            minutes Integer,
            shiftdate Text,
            employee_id Integer,
            FOREIGN KEY (employee_id)
                REFERENCES employees(id)
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insertShift(self, minutes, idp):
        #emp = self.fetchEmployee(idp)
        now = datetime.now()
        date = now.strftime('%d/%m/%Y')
        self.cur.execute("insert into shifts values (NULL,?,?,?)",
                         (minutes, date, idp))
        self.con.commit()

    def insertEmployee(self, name, birthdate, phone, banknum, hourlyrate):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?)",
                         (name, birthdate, phone, banknum, hourlyrate))
        self.con.commit()

    # Update a Record in DB
    def updateEmployee(self, id, name, birthdate, phone, banknum, hourlyrate):
        self.cur.execute(
            "update employees set name=?, birthdate=?, phone=?, banknum=?, hourlyrate=? where id=?",
            (name, birthdate, phone, banknum, hourlyrate, id))
        self.con.commit()

    # Fetch All Data from DB
    def fetchEmployees(self):
        self.cur.execute("SELECT employees.id, employees.name from employees")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    def fetchShifts(self,idp):
        self.cur.execute("""SELECT shifts.ids, shifts.shiftdate, round(employees.hourlyrate / 60 * shifts.minutes, 2) AS due, (shifts.minutes - (shifts.minutes % 60)) / 60 AS hours, shifts.minutes % 60 AS minutes
                            FROM employees 
                            INNER JOIN shifts ON employees.id = shifts.employee_id
                            WHERE employees.id=?""", [idp])
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    def fetchSumShifts(self, idp):
        self.cur.execute("""SELECT round(Sum((employees.hourlyrate / 60 * shifts.minutes)), 2)
                                    FROM employees 
                                    INNER JOIN shifts ON employees.id = shifts.employee_id
                                    WHERE employees.id=?""", [idp])
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    def mngFetchEmployees(self):
        self.cur.execute("""SELECT employees.id, employees.name, employees.birthdate, employees.phone, employees.banknum, employees.hourlyrate, round(Sum((employees.hourlyrate / 60 * shifts.minutes)), 2) AS toPay
                            FROM employees
                            LEFT JOIN shifts ON employees.id = shifts.employee_id
                            GROUP BY employees.name, employees.id""")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    # Delete a Record in DB
    def removeEmployee(self, id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.con.commit()

    def deleteAllShifts(self):
        self.cur.execute("delete from shifts")
        self.con.commit()
