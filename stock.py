from tkinter import *
from tkinter import ttk, messagebox
from db import Database


class StockClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+220+130")
        self.root.title("Stock Details")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = Database()

        # ================= Variables =================

        self.var_search = StringVar()

        # ================= Title =================

        title = Label(
            self.root,
            text="Stock Management",
            font=("Arial", 18, "bold"),
            bg="#0f4d7d",
            fg="white"
        )
        title.pack(side=TOP, fill=X)

        # ================= Search Frame =================

        searchFrame = Frame(
            self.root,
            bd=2,
            relief=RIDGE,
            bg="white"
        )
        searchFrame.place(x=20, y=60, width=1060, height=60)

        Label(
            searchFrame,
            text="Search Product",
            font=("Arial", 13, "bold"),
            bg="white"
        ).place(x=20, y=15)

        Entry(
            searchFrame,
            textvariable=self.var_search,
            font=("Arial", 12),
            bg="lightyellow"
        ).place(x=170, y=15, width=250)

        Button(
            searchFrame,
            text="Search",
            command=self.search,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        ).place(x=450, y=12, width=120, height=30)

        Button(
            searchFrame,
            text="Show All",
            command=self.show,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        ).place(x=590, y=12, width=120, height=30)

        # ================= Stock Details =================

        stockFrame = Frame(
            self.root,
            bd=3,
            relief=RIDGE
        )
        stockFrame.place(x=20, y=140, width=1060, height=380)

        scrollx = Scrollbar(
            stockFrame,
            orient=HORIZONTAL
        )

        scrolly = Scrollbar(
            stockFrame,
            orient=VERTICAL
        )

        self.StockTable = ttk.Treeview(
            stockFrame,
            columns=(
                "pid",
                "name",
                "brand",
                "qty",
                "reorder",
                "status"
            ),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.StockTable.xview)
        scrolly.config(command=self.StockTable.yview)

        self.StockTable.heading("pid", text="Product ID")
        self.StockTable.heading("name", text="Product Name")
        self.StockTable.heading("brand", text="Brand")
        self.StockTable.heading("qty", text="Stock Qty")
        self.StockTable.heading("reorder", text="Reorder Level")
        self.StockTable.heading("status", text="Stock Status")

        self.StockTable["show"] = "headings"

        self.StockTable.column("pid", width=100)
        self.StockTable.column("name", width=250)
        self.StockTable.column("brand", width=180)
        self.StockTable.column("qty", width=120)
        self.StockTable.column("reorder", width=120)
        self.StockTable.column("status", width=180)

        self.StockTable.pack(fill=BOTH, expand=1)

        self.show()

    # ================= Show Stock =================

    def show(self):
        try:

            self.db.execute("""
                SELECT
                    product_id,
                    product_name,
                    brand,
                    quantity,
                    reorder_level
                FROM product
                ORDER BY product_name
            """)

            rows = self.db.fetchall()

            self.StockTable.delete(*self.StockTable.get_children())

            for row in rows:

                qty = int(row[3])
                reorder = int(row[4])

                if qty == 0:
                    status = "Out Of Stock"

                elif qty <= reorder:
                    status = "Low Stock"

                else:
                    status = "Available"

                self.StockTable.insert(
                    "",
                    END,
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        qty,
                        reorder,
                        status
                    )
                )

        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex),
                parent=self.root
            )

    # ================= Search =================

    def search(self):

        if self.var_search.get() == "":
            self.show()
            return

        try:

            self.db.execute(
                """
                SELECT
                    product_id,
                    product_name,
                    brand,
                    quantity,
                    reorder_level
                FROM product
                WHERE product_name LIKE %s
                ORDER BY product_name
                """,
                (
                    "%" + self.var_search.get() + "%",
                )
            )

            rows = self.db.fetchall()

            self.StockTable.delete(*self.StockTable.get_children())

            for row in rows:

                qty = int(row[3])
                reorder = int(row[4])

                if qty == 0:
                    status = "Out Of Stock"

                elif qty <= reorder:
                    status = "Low Stock"

                else:
                    status = "Available"

                self.StockTable.insert(
                    "",
                    END,
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        qty,
                        reorder,
                        status
                    )
                )

        except Exception as ex:
            messagebox.showerror(
                "Error",
                str(ex),
                parent=self.root
            )

if __name__ == "__main__":
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()