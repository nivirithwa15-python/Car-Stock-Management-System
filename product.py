from tkinter import *
from tkinter import ttk, messagebox
from db import Database


class ProductClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+220+130")
        self.root.title("Product Details")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = Database()

        # ================= Variables =================
        self.var_pid = StringVar()
        self.var_category = StringVar()
        self.var_supplier = StringVar()
        self.var_name = StringVar()
        self.var_brand = StringVar()
        self.var_vehicle = StringVar()
        self.var_purchase = StringVar()
        self.var_selling = StringVar()
        self.var_qty = StringVar()
        self.var_reorder = StringVar()
        self.var_barcode = StringVar()

        self.category_list = []
        self.supplier_list = []

        # ================= Title =================

        title = Label(
            self.root,
            text="Manage Product Details",
            font=("Arial", 18, "bold"),
            bg="#0f4d7d",
            fg="white"
        )
        title.pack(side=TOP, fill=X)

        # ================= Product Frame =================

        productFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        productFrame.place(x=10, y=50, width=450, height=480)

        # Category
        Label(productFrame, text="Category", font=("Arial", 13), bg="white").place(x=20, y=20)

        self.cmb_category = ttk.Combobox(
            productFrame,
            textvariable=self.var_category,
            state="normal",
            font=("Arial", 12)
        )
        self.cmb_category.place(x=170, y=20, width=240)

        # Supplier
        Label(productFrame, text="Supplier", font=("Arial", 13), bg="white").place(x=20, y=60)

        self.cmb_supplier = ttk.Combobox(
            productFrame,
            textvariable=self.var_supplier,
            state="normal",
            font=("Arial", 12)
        )
        self.cmb_supplier.place(x=170, y=60, width=240)

        # Product Name
        Label(productFrame, text="Product Name", font=("Arial", 13), bg="white").place(x=20, y=100)
        Entry(productFrame, textvariable=self.var_name, font=("Arial", 12), bg="lightyellow").place(x=170, y=100,
                                                                                                    width=240)

        # Brand
        Label(productFrame, text="Brand", font=("Arial", 13), bg="white").place(x=20, y=140)
        Entry(productFrame, textvariable=self.var_brand, font=("Arial", 12), bg="lightyellow").place(x=170, y=140,
                                                                                                     width=240)

        # Vehicle Model
        Label(productFrame, text="Vehicle Model", font=("Arial", 13), bg="white").place(x=20, y=180)
        Entry(productFrame, textvariable=self.var_vehicle, font=("Arial", 12), bg="lightyellow").place(x=170, y=180,
                                                                                                       width=240)

        # Purchase Price
        Label(productFrame, text="Purchase Price", font=("Arial", 13), bg="white").place(x=20, y=220)
        Entry(productFrame, textvariable=self.var_purchase, font=("Arial", 12), bg="lightyellow").place(x=170, y=220,
                                                                                                        width=240)

        # Selling Price
        Label(productFrame, text="Selling Price", font=("Arial", 13), bg="white").place(x=20, y=260)
        Entry(productFrame, textvariable=self.var_selling, font=("Arial", 12), bg="lightyellow").place(x=170, y=260,
                                                                                                       width=240)

        # Quantity
        Label(productFrame, text="Quantity", font=("Arial", 13), bg="white").place(x=20, y=300)
        Entry(productFrame, textvariable=self.var_qty, font=("Arial", 12), bg="lightyellow").place(x=170, y=300,
                                                                                                   width=240)

        # Reorder Level
        Label(productFrame, text="Reorder Level", font=("Arial", 13), bg="white").place(x=20, y=340)
        Entry(productFrame, textvariable=self.var_reorder, font=("Arial", 12), bg="lightyellow").place(x=170, y=340,
                                                                                                       width=240)

        # Barcode
        Label(productFrame, text="Barcode", font=("Arial", 13), bg="white").place(x=20, y=380)
        Entry(productFrame, textvariable=self.var_barcode, font=("Arial", 12), bg="lightyellow").place(x=170, y=380,
                                                                                                       width=240)
        # ================= Buttons =================

        Button(
            productFrame,
            text="Save",
            command=self.add,
            font=("Arial", 12, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2"
        ).place(x=20, y=430, width=90, height=30)

        Button(
            productFrame,
            text="Update",
            command=self.update,
            font=("Arial", 12, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2"
        ).place(x=120, y=430, width=90, height=30)

        Button(
            productFrame,
            text="Delete",
            command=self.delete,
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2"
        ).place(x=220, y=430, width=90, height=30)

        Button(
            productFrame,
            text="Clear",
            command=self.clear,
            font=("Arial", 12, "bold"),
            bg="#607d8b",
            fg="white",
            cursor="hand2"
        ).place(x=320, y=430, width=90, height=30)

        # ================= Product Details =================

        detailsFrame = Frame(self.root, bd=3, relief=RIDGE)
        detailsFrame.place(x=470, y=50, width=620, height=480)

        scrollx = Scrollbar(detailsFrame, orient=HORIZONTAL)
        scrolly = Scrollbar(detailsFrame, orient=VERTICAL)

        self.ProductTable = ttk.Treeview(
            detailsFrame,
            columns=(
                "pid",
                "name",
                "category",
                "supplier",
                "brand",
                "vehicle",
                "purchase",
                "selling",
                "qty",
                "reorder",
                "barcode"
            ),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid", text="ID")
        self.ProductTable.heading("name", text="Product")
        self.ProductTable.heading("category", text="Category")
        self.ProductTable.heading("supplier", text="Supplier")
        self.ProductTable.heading("brand", text="Brand")
        self.ProductTable.heading("vehicle", text="Vehicle")
        self.ProductTable.heading("purchase", text="Purchase")
        self.ProductTable.heading("selling", text="Selling")
        self.ProductTable.heading("qty", text="Qty")
        self.ProductTable.heading("reorder", text="Reorder")
        self.ProductTable.heading("barcode", text="Barcode")

        self.ProductTable.column("pid", width=60)
        self.ProductTable.column("name", width=150)
        self.ProductTable.column("category", width=120)
        self.ProductTable.column("supplier", width=150)
        self.ProductTable.column("brand", width=100)
        self.ProductTable.column("vehicle", width=120)
        self.ProductTable.column("purchase", width=90)
        self.ProductTable.column("selling", width=90)
        self.ProductTable.column("qty", width=70)
        self.ProductTable.column("reorder", width=90)
        self.ProductTable.column("barcode", width=130)
        self.ProductTable["show"] = "headings"

        self.ProductTable.pack(fill=BOTH, expand=1)

        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)

        # ================= Fetch Data ================= #
        self.fetch_category()
        self.fetch_supplier()

        self.cmb_category["values"] = self.category_list
        self.cmb_supplier["values"] = self.supplier_list

        self.cmb_category.current(0)
        self.cmb_supplier.current(0)

        self.show()

        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)

    def fetch_category(self):
        self.category_list = []

        query = "SELECT category_name FROM category"

        if self.db.execute(query):
            rows = self.db.fetchall()

            self.category_list.append("Select")

            for row in rows:
                self.category_list.append(row[0])

        print("Category List:", self.category_list)

    def fetch_supplier(self):
        self.supplier_list = []

        query = "SELECT supplier_name FROM supplier"

        if self.db.execute(query):
            rows = self.db.fetchall()

            self.supplier_list.append("Select")

            for row in rows:
                self.supplier_list.append(row[0])

        print("Supplier List:", self.supplier_list)

    def add(self):
        if self.var_category.get() == "Select" or \
                self.var_supplier.get() == "Select" or \
                self.var_name.get() == "":
            messagebox.showerror(
                "Error",
                "Category, Supplier and Product Name are required",
                parent=self.root
            )
            return

        # ---------- Category ----------

        self.db.execute(
            "SELECT category_id FROM category WHERE category_name=%s",
            (self.var_category.get().strip(),)
        )

        cat = self.db.fetchone()

        if not cat:

            self.db.execute(
                "INSERT INTO category(category_name) VALUES(%s)",
                (self.var_category.get().strip(),)
            )

            self.db.con.commit()

            self.db.execute(
                "SELECT category_id FROM category WHERE category_name=%s",
                (self.var_category.get().strip(),)
            )

            cat = self.db.fetchone()

            self.fetch_category()
            self.cmb_category["values"] = self.category_list

        # ---------- Supplier ----------

        self.db.execute(
            "SELECT supplier_id FROM supplier WHERE supplier_name=%s",
            (self.var_supplier.get().strip(),)
        )

        sup = self.db.fetchone()

        if not sup:

            self.db.execute(
                """
                INSERT INTO supplier(supplier_name)
                VALUES(%s)
                """,
                (self.var_supplier.get().strip(),)
            )

            self.db.con.commit()

            self.db.execute(
                "SELECT supplier_id FROM supplier WHERE supplier_name=%s",
                (self.var_supplier.get().strip(),)
            )

            sup = self.db.fetchone()

            self.fetch_supplier()
            self.cmb_supplier["values"] = self.supplier_list

        query = """
        INSERT INTO product
        (product_name, category_id, supplier_id, brand,
        vehicle_model, purchase_price, selling_price,
        quantity, reorder_level, barcode)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            self.var_name.get(),
            cat[0],
            sup[0],
            self.var_brand.get(),
            self.var_vehicle.get(),
            self.var_purchase.get(),
            self.var_selling.get(),
            self.var_qty.get(),
            self.var_reorder.get(),
            self.var_barcode.get(),
        )
        print("VALUES =", values)
        print("QUERY EXECUTING...")

        if self.db.execute(query, values):
            messagebox.showinfo(
                "Success",
                "Product Added Successfully",
                parent=self.root
            )
            self.show()
            self.clear()

    def show(self):
        self.ProductTable.delete(*self.ProductTable.get_children())

        query = """
        SELECT
            p.product_id,
            p.product_name,
            c.category_name,
            s.supplier_name,
            p.brand,
            p.vehicle_model,
            p.purchase_price,
            p.selling_price,
            p.quantity,
            p.reorder_level,
            p.barcode,
            p.description
        FROM product p
        LEFT JOIN category c ON p.category_id = c.category_id
        LEFT JOIN supplier s ON p.supplier_id = s.supplier_id
        ORDER BY p.product_id DESC
        """

        if self.db.execute(query):
            rows = self.db.fetchall()

            for row in rows:
                self.ProductTable.insert("", END, values=row)

    def clear(self):
        self.var_pid.set("")
        self.var_category.set("Select")
        self.var_supplier.set("Select")
        self.var_name.set("")
        self.var_brand.set("")
        self.var_vehicle.set("")
        self.var_purchase.set("")
        self.var_selling.set("")
        self.var_qty.set("")
        self.var_reorder.set("")
        self.var_barcode.set("")

        self.show()

    def get_data(self, ev):
        f = self.ProductTable.focus()
        content = self.ProductTable.item(f)
        row = content["values"]

        if row:
            self.var_pid.set(row[0])
            self.var_name.set(row[1])
            self.var_category.set(row[2])
            self.var_supplier.set(row[3])
            self.var_brand.set(row[4])
            self.var_vehicle.set(row[5])
            self.var_purchase.set(row[6])
            self.var_selling.set(row[7])
            self.var_qty.set(row[8])
            self.var_reorder.set(row[9])
            self.var_barcode.set(row[10])

    def update(self):

        if self.var_pid.get() == "":
            messagebox.showerror(
                "Error",
                "Please Select Product",
                parent=self.root
            )
            return

        try:

            # Category
            self.db.execute(
                "SELECT category_id FROM category WHERE category_name=%s",
                (self.var_category.get(),)
            )
            cat = self.db.fetchone()

            # Supplier
            self.db.execute(
                "SELECT supplier_id FROM supplier WHERE supplier_name=%s",
                (self.var_supplier.get(),)
            )
            sup = self.db.fetchone()

            if not cat or not sup:
                messagebox.showerror(
                    "Error",
                    "Invalid Category or Supplier",
                    parent=self.root
                )
                return

            self.db.execute(
                """
                UPDATE product
                SET
                    product_name=%s,
                    category_id=%s,
                    supplier_id=%s,
                    brand=%s,
                    vehicle_model=%s,
                    purchase_price=%s,
                    selling_price=%s,
                    quantity=%s,
                    reorder_level=%s,
                    barcode=%s
                WHERE product_id=%s
                """,
                (
                    self.var_name.get(),
                    cat[0],
                    sup[0],
                    self.var_brand.get(),
                    self.var_vehicle.get(),
                    self.var_purchase.get(),
                    self.var_selling.get(),
                    self.var_qty.get(),
                    self.var_reorder.get(),
                    self.var_barcode.get(),
                    self.var_pid.get()
                )
            )

            messagebox.showinfo(
                "Success",
                "Product Updated Successfully",
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

    def delete(self):

        if self.var_pid.get() == "":
            messagebox.showerror(
                "Error",
                "Please Select Product",
                parent=self.root
            )
            return

        confirm = messagebox.askyesno(
            "Delete",
            "Do you want to delete this Product?",
            parent=self.root
        )

        if confirm:
            self.db.execute(
                "DELETE FROM product WHERE product_id=%s",
                (self.var_pid.get(),)
            )

            messagebox.showinfo(
                "Success",
                "Product Deleted Successfully",
                parent=self.root
            )

            self.show()
            self.clear()

if __name__ == "__main__":
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()