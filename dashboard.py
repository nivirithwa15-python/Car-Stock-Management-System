from tkinter import *
from tkinter import messagebox
from supplier import SupplierClass
from category import CategoryClass
from product import ProductClass
from employee import EmployeeClass
from sales import SalesClass
from stock import StockClass
from db import Database
from time import strftime
from datetime import datetime


class IMS:
    def __init__(self, root ):
        self.root = root
        self.root.title("CAR SPARE PARTS - STOCK MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.resizable(True, True)
        self.db = Database()

        # ================= Title =================
        title = Label(
            self.root,
            text="CAR SPARE PARTS - STOCK MANAGEMENT SYSTEM",
            font=("Arial", 24, "bold"),
            bg="#263238",
            fg="white",
            padx=20,
            pady=10
        )
        title.pack(fill=X)

        # ================= Clock =================
        self.lbl_clock = Label(
            self.root,
            text="",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#263238"
        )
        self.lbl_clock.place(x=240, y=65)

        self.update_time()

        # ================= Left Menu =================
        menu_frame = Frame(self.root, bg="#1b1b1b", bd=2, relief=RIDGE)
        menu_frame.place(x=0, y=60, width=220, height=640)

        menu_title = Label(
            menu_frame,
            text="MENU",
            font=("Arial", 20, "bold"),
            bg="#263238",
            fg="white"
        )
        menu_title.pack(pady=15)
        Button(menu_frame, text="Dashboard", font=("Arial", 14), width=18).pack(pady=5)

        Button(
            menu_frame,
            text="Supplier",
            font=("Arial", 14),
            width=18,
            command=self.supplier
        ).pack(pady=5)

        Button(
            menu_frame,
            text="Category",
            font=("Arial", 14),
            width=18,
            command=self.category
        ).pack(pady=5)

        Button(
            menu_frame,
            text="Product",
            font=("Arial", 14),
            width=18,
            command=self.product
        ).pack(pady=5)

        Button(
            menu_frame,
            text="Employee",
            font=("Arial", 14),
            width=18,
            command=self.employee
        ).pack(pady=5)

        Button(
            menu_frame,
            text="Sales",
            font=("Arial", 14),
            width=18,
            command=self.sales
        ).pack(pady=5)

        Button(
            menu_frame,
            text="Stock",
            font=("Arial", 14),
            width=18,
            command=self.stock
        ).pack(pady=5)

        Button(
            menu_frame,
            text="Exit",
            font=("Arial", 14),
            width=18,
             command=self.exit_app
        ).pack(pady=5)

        # ================= Dashboard =================
        dashboard = Frame(self.root, bg="white")
        dashboard.place(x=240, y=110, width=1080, height=500)
        self.supplier_box = Label(
            dashboard,
            text="SUPPLIER\n\n0",
            font=("Arial", 18, "bold"),
            bg="#4CAF50",
            fg="white",
            width=15,
            height=5
        )
        self.supplier_box.grid(row=0, column=0, padx=20, pady=20)

        self.category_box = Label(
            dashboard,
            text="CATEGORY\n\n0",
            font=("Arial", 18, "bold"),
            bg="#FF9800",
            fg="white",
            width=15,
            height=5
        )
        self.category_box.grid(row=0, column=1, padx=20, pady=20)

        self.product_box = Label(
            dashboard,
            text="PRODUCT\n\n0",
            font=("Arial", 18, "bold"),
            bg="#2196F3",
            fg="white",
            width=15,
            height=5
        )
        self.product_box.grid(row=0, column=2, padx=20, pady=20)

        self.employee_box = Label(
            dashboard,
            text="EMPLOYEE\n\n0",
            font=("Arial", 18, "bold"),
            bg="#9C27B0",
            fg="white",
            width=15,
            height=5
        )
        self.employee_box.grid(row=1, column=0, padx=20, pady=20)

        self.sales_box = Label(
            dashboard,
            text="SALES\n\n0",
            font=("Arial", 18, "bold"),
            bg="#E91E63",
            fg="white",
            width=15,
            height=5
        )
        self.sales_box.grid(row=1, column=1, padx=20, pady=20)

        self.stock_box = Label(
            dashboard,
            text="STOCK\n\n0",
            font=("Arial", 18, "bold"),
            bg="#607D8B",
            fg="white",
            width=15,
            height=5
        )
        self.stock_box.grid(row=1, column=2, padx=20, pady=20)
        self.update_dashboard()

        # ================= Footer =================
        footer = Label(
            self.root,
            text="Car Spare Parts - Stock Management System | Developed by Nivethitha",
            font=("Arial", 12),
            bg="#263238",
            fg="white"
        )
        footer.pack(side=BOTTOM, fill=X)

    def update_dashboard(self):
        try:
            # Supplier Count
            self.db.execute("SELECT COUNT(*) FROM supplier")
            supplier = self.db.fetchone()[0]
            self.supplier_box.config(text=f"SUPPLIER\n\n{supplier}")

            # Category Count
            self.db.execute("SELECT COUNT(*) FROM category")
            category = self.db.fetchone()[0]
            self.category_box.config(text=f"CATEGORY\n\n{category}")

            # Product Count
            self.db.execute("SELECT COUNT(*) FROM product")
            product = self.db.fetchone()[0]
            self.product_box.config(text=f"PRODUCT\n\n{product}")

            # Employee Count
            self.db.execute("SELECT COUNT(*) FROM employee")
            employee = self.db.fetchone()[0]
            self.employee_box.config(text=f"EMPLOYEE\n\n{employee}")

            # Sales Count
            self.db.execute("SELECT COUNT(*) FROM sales")
            sales = self.db.fetchone()[0]
            self.sales_box.config(text=f"SALES\n\n{sales}")

            # Stock Count
            self.db.execute("SELECT SUM(quantity) FROM product")
            stock = self.db.fetchone()[0]

            if stock is None:
                stock = 0

            self.stock_box.config(text=f"STOCK\n\n{stock}")


        except Exception as ex:
            print("Dashboard Error:", ex)

    def update_time(self):
            time_ = strftime("%I:%M:%S %p")
            date_ = datetime.now().strftime("%d-%m-%Y")
            self.lbl_clock.config(
                text=f"Welcome to Car Spare Parts Stock Management System\t\tDate: {date_}\t\tTime: {time_}"
            )
            self.lbl_clock.after(1000, self.update_time)

    def supplier(self):
            new_win = Toplevel(self.root)
            SupplierClass(new_win)

    def category(self):
            new_win = Toplevel(self.root)
            CategoryClass(new_win)

    def product(self):
            new_win = Toplevel(self.root)
            ProductClass(new_win)

    def employee(self):
            new_win = Toplevel(self.root)
            EmployeeClass(new_win)

    def sales(self):
        new_win = Toplevel(self.root)
        SalesClass(new_win)

    def stock(self):
        new_win = Toplevel(self.root)
        StockClass(new_win)

    def exit_app(self):

        confirm = messagebox.askyesno(
            "Exit",
            "Do you want to Exit the Application?",
            parent=self.root
        )

        if confirm:
            self.root.destroy()
