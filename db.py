import mysql.connector
from tkinter import messagebox


class Database:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="YOUR_MYSQL_PASSWORD",
                database="car_spare_parts_stock_management_system"
            )

            self.cur = self.con.cursor(buffered=True)
            print("Database Connected Successfully")

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def execute(self, query, values=None):
        try:
            if values:
                self.cur.execute(query, values)
            else:
                self.cur.execute(query)

            self.con.commit()
            return True

        except Exception as e:
            print(e)
            return False

    def fetchone(self):
        return self.cur.fetchone()

    def fetchall(self):
        return self.cur.fetchall()

    def close(self):
        self.con.close()




