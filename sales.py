from tkinter import *
from tkinter import ttk, messagebox
from db import Database
from datetime import datetime


class SalesClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+220+130")
        self.root.title("Sales Details")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = Database()

        # ================= Variables =================

        self.var_sale_id = StringVar()
        self.var_customer = StringVar()
        self.var_date = StringVar()
        self.var_total = StringVar()

        self.customer_list = []

        # Today's Date
        self.var_date.set(datetime.now().strftime("%Y-%m-%d"))

        # ================= Title =================

        title = Label(
            self.root,
            text="Manage Sales Details",
            font=("Arial", 18, "bold"),
            bg="#0f4d7d",
            fg="white"
        )
        title.pack(side=TOP, fill=X)

        # ================= Left Frame =================

        salesFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        salesFrame.place(x=10, y=50, width=420, height=480)

        # Sale ID

        Label(
            salesFrame,
            text="Sale ID",
            font=("Arial", 13),
            bg="white"
        ).place(x=20, y=30)

        txt_sale = Entry(
            salesFrame,
            textvariable=self.var_sale_id,
            font=("Arial", 12),
            bg="lightyellow"
        )
        txt_sale.place(x=170, y=30, width=200)

        # Customer

        Label(
            salesFrame,
            text="Customer",
            font=("Arial", 13),
            bg="white"
        ).place(x=20, y=90)

        self.cmb_customer = ttk.Combobox(
            salesFrame,
            textvariable=self.var_customer,
            state="normal",
            font=("Arial", 12)
        )

        self.cmb_customer.place(x=170, y=90, width=200)

        # Sale Date

        Label(
            salesFrame,
            text="Sale Date",
            font=("Arial", 13),
            bg="white"
        ).place(x=20, y=150)

        txt_date = Entry(
            salesFrame,
            textvariable=self.var_date,
            font=("Arial", 12),
            bg="lightyellow"
        )

        txt_date.place(x=170, y=150, width=200)

        # Total Amount

        Label(
            salesFrame,
            text="Total Amount",
            font=("Arial", 13),
            bg="white"
        ).place(x=20, y=210)

        txt_total = Entry(
            salesFrame,
            textvariable=self.var_total,
            font=("Arial", 12),
            bg="lightyellow"
        )

        txt_total.place(x=170, y=210, width=200)

        # ================= Buttons =================

        Button(
            salesFrame,
            text="Save",
            command=self.add,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        ).place(x=20, y=300, width=80, height=35)

        Button(
            salesFrame,
            text="Update",
            command=self.update,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        ).place(x=110, y=300, width=80, height=35)

        Button(
            salesFrame,
            text="Delete",
            command=self.delete,
            font=("Arial", 12, "bold"),
            bg="#F44336",
            fg="white",
            cursor="hand2"
        ).place(x=200, y=300, width=80, height=35)

        Button(
            salesFrame,
            text="Clear",
            command=self.clear,
            font=("Arial", 12, "bold"),
            bg="#607D8B",
            fg="white",
            cursor="hand2"
        ).place(x=290, y=300, width=80, height=35)

        # ================= Right Frame =================

        detailsFrame = Frame(self.root, bd=3, relief=RIDGE)
        detailsFrame.place(x=450, y=50, width=640, height=480)

        scrollx = Scrollbar(detailsFrame, orient=HORIZONTAL)
        scrolly = Scrollbar(detailsFrame, orient=VERTICAL)

        self.SalesTable = ttk.Treeview(
            detailsFrame,
            columns=("saleid", "customer", "date", "total"),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.SalesTable.xview)
        scrolly.config(command=self.SalesTable.yview)

        self.SalesTable.heading("saleid", text="Sale ID")
        self.SalesTable.heading("customer", text="Customer Name")
        self.SalesTable.heading("date", text="Sale Date")
        self.SalesTable.heading("total", text="Total Amount")

        self.SalesTable["show"] = "headings"

        self.SalesTable.column("saleid", width=80)
        self.SalesTable.column("customer", width=120)
        self.SalesTable.column("date", width=120)
        self.SalesTable.column("total", width=120)

        self.SalesTable.pack(fill=BOTH, expand=1)

        self.fetch_customer()

        self.cmb_customer["values"] = self.customer_list

        self.show()

        self.SalesTable.bind("<ButtonRelease-1>", self.get_data)

# ================= Customer List =================

    def fetch_customer(self):
        self.customer_list.clear()
        self.customer_list.append("Select")

        try:
            self.db.execute(
                "SELECT customer_id, customer_name FROM customer ORDER BY customer_name"
            )

            rows = self.db.fetchall()

            print(rows)

            for row in rows:
                self.customer_list.append(f"{row[0]} - {row[1]}")

            print(self.customer_list)

        except Exception as ex:
            print("Customer Fetch Error:", ex)

    # ================= Show Data =================

    def show(self):
        try:
            self.db.execute("""
                SELECT s.sale_id,
                       c.customer_name,
                       s.sale_date,
                       s.total_amount
                FROM sales s
                INNER JOIN customer c
                    ON s.customer_id = c.customer_id
                ORDER BY s.sale_id DESC
            """)
            rows = self.db.fetchall()

            self.SalesTable.delete(*self.SalesTable.get_children())

            for row in rows:
                self.SalesTable.insert("", END, values=row)

        except Exception as ex:
            print("Show Error:", ex)

    # ================= Add Sale =================

    def add(self):
        if self.var_customer.get() == "Select" or self.var_customer.get() == "":
            messagebox.showerror("Error", "Please Select Customer", parent=self.root)
            return

        if self.var_total.get() == "":
            messagebox.showerror("Error", "Enter Total Amount", parent=self.root)
            return

        try:
            customer_name = self.var_customer.get().strip()

            # Check customer exists
            self.db.execute(
                "SELECT customer_id FROM customer WHERE customer_name=%s",
                (customer_name,)
            )

            row = self.db.fetchone()

            if row:
                customer_id = row[0]
            else:
                # Add new customer
                self.db.execute(
                    "INSERT INTO customer(customer_name) VALUES(%s)",
                    (customer_name,)
                )

                self.db.con.commit()

                self.db.execute(
                    "SELECT customer_id FROM customer WHERE customer_name=%s",
                    (customer_name,)
                )

                customer_id = self.db.fetchone()[0]

                # Refresh dropdown
                self.fetch_customer()
                self.cmb_customer["values"] = self.customer_list

            self.db.execute(
                """
                INSERT INTO sales
                (customer_id, sale_date, total_amount)
                VALUES (%s,%s,%s)
                """,
                (
                    customer_id,
                    self.var_date.get(),
                    self.var_total.get()
                )
            )

            self.db.con.commit()

            messagebox.showinfo(
                "Success",
                "Sale Added Successfully",
                parent=self.root
            )

            self.show()
            self.clear()

        except Exception as ex:
            messagebox.showerror("Error", str(ex), parent=self.root)

    #====================Get Data================

    def get_data(self, ev):
        f = self.SalesTable.focus()

        content = self.SalesTable.item(f)

        row = content["values"]

        if row:
            self.var_sale_id.set(row[0])
            self.var_customer.set(row[1])
            self.var_date.set(row[2])
            self.var_total.set(row[3])

    # ================= Update Sale =================

    def update(self):
        if self.var_sale_id.get() == "":
            messagebox.showerror(
                "Error",
                "Please Select Sale",
                parent=self.root
            )
            return

        try:
            customer_name = self.var_customer.get().strip()

            self.db.execute(
                "SELECT customer_id FROM customer WHERE customer_name=%s",
                (customer_name,)
            )

            row = self.db.fetchone()

            if row:
                customer_id = row[0]
            else:
                self.db.execute(
                    "INSERT INTO customer(customer_name) VALUES(%s)",
                    (customer_name,)
                )

                self.db.con.commit()

                self.db.execute(
                    "SELECT customer_id FROM customer WHERE customer_name=%s",
                    (customer_name,)
                )

                customer_id = self.db.fetchone()[0]

                self.fetch_customer()
                self.cmb_customer["values"] = self.customer_list

            self.db.execute(
                """
                UPDATE sales
                SET customer_id=%s,
                    sale_date=%s,
                    total_amount=%s
                WHERE sale_id=%s
                """,
                (
                    customer_id,
                    self.var_date.get(),
                    self.var_total.get(),
                    self.var_sale_id.get()
                )
            )

            self.db.con.commit()

            messagebox.showinfo(
                "Success",
                "Sale Updated Successfully",
                parent=self.root
            )

            self.show()
            self.clear()

        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex),
                parent=self.root
            )

    # ================= Clear =================

    def clear(self):
        self.var_sale_id.set("")
        self.var_customer.set("Select")
        self.var_date.set(datetime.now().strftime("%Y-%m-%d"))
        self.var_total.set("")

    # ================= Delete Sale =================

    def delete(self):
        if self.var_sale_id.get() == "":
            messagebox.showerror(
                "Error",
                "Please Select Sale",
                parent=self.root
            )
            return

        confirm = messagebox.askyesno(
            "Delete",
            "Do you really want to delete this Sale?",
            parent=self.root
        )

        if confirm:
            try:
                self.db.execute(
                    "DELETE FROM sales WHERE sale_id=%s",
                    (self.var_sale_id.get(),)
                )

                self.db.con.commit()

                messagebox.showinfo(
                    "Success",
                    "Sale Deleted Successfully",
                    parent=self.root
                )

                self.show()
                self.clear()

            except Exception as ex:
                messagebox.showerror(
                    "Error",
                    str(ex),
                    parent=self.root
                )
if __name__ == "__main__":
    root = Tk()
    obj = SalesClass(root)
    root.mainloop()





