from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db import Database


class SupplierClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Supplier Details")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = Database()

        # ================= Variables =================
        self.var_supplier_name = StringVar()
        self.var_company_name = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_gst = StringVar()
        self.var_search = StringVar()

        # ================= Title =================
        title = Label(
            self.root,
            text="Manage Supplier Details",
            font=("Arial", 20, "bold"),
            bg="#0f4d7d",
            fg="white"
        )
        title.pack(side=TOP, fill=X)

        # ================= Labels =================
        Label(
            self.root,
            text="Supplier Name",
            font=("Arial", 15),
            bg="white"
        ).place(x=50, y=80)

        Label(
            self.root,
            text="Company Name",
            font=("Arial", 15),
            bg="white"
        ).place(x=50, y=140)

        Label(
            self.root,
            text="Phone",
            font=("Arial", 15),
            bg="white"
        ).place(x=50, y=200)

        Label(
            self.root,
            text="Email",
            font=("Arial", 15),
            bg="white"
        ).place(x=50, y=260)

        Label(
            self.root,
            text="GST Number",
            font=("Arial", 15),
            bg="white"
        ).place(x=50, y=320)

        Label(
            self.root,
            text="Address",
            font=("Arial", 15),
            bg="white"
        ).place(x=50, y=380)

        # ================= Entry =================
        Entry(
            self.root,
            textvariable=self.var_supplier_name,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=230, y=80, width=300)

        Entry(
            self.root,
            textvariable=self.var_company_name,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=230, y=140, width=300)

        Entry(
            self.root,
            textvariable=self.var_phone,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=230, y=200, width=300)

        Entry(
            self.root,
            textvariable=self.var_email,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=230, y=260, width=300)

        Entry(
            self.root,
            textvariable=self.var_gst,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=230, y=320, width=300)

        self.txt_address = Text(
            self.root,
            font=("Arial", 15),
            bg="lightyellow"
        )
        self.txt_address.place(x=230, y=380, width=350, height=120)

        # ================= Buttons =================
        btn_save = Button(
            self.root,
            text="Save",
            command=self.add,
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        )
        btn_save.place(x=650, y=80, width=150, height=40)

        btn_update = Button(
            self.root,
            text="Update",
            command=self.update,
            font=("Arial", 14, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        btn_update.place(x=650, y=140, width=150, height=40)

        btn_delete = Button(
            self.root,
            text="Delete",
            command=self.delete,
            font=("Arial", 14, "bold"),
            bg="#F44336",
            fg="white",
            cursor="hand2"
        )
        btn_delete.place(x=650, y=200, width=150, height=40)

        btn_clear = Button(
            self.root,
            text="Clear",
            command=self.clear,
            font=("Arial", 14, "bold"),
            bg="#607D8B",
            fg="white",
            cursor="hand2"
        )
        btn_clear.place(x=650, y=260, width=150, height=40)

        # ================= Search =================
        Label(
            self.root,
            text="Search",
            font=("Arial", 15),
            bg="white"
        ).place(x=620, y=340)

        Entry(
            self.root,
            textvariable=self.var_search,
            font=("Arial", 14),
            bg="lightyellow"
        ).place(x=700, y=340, width=180)

        Button(
            self.root,
            text="Search",
            command=self.search,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        ).place(x=900, y=338, width=100, height=32)

        # ================= Supplier Details =================

        frame = Frame(self.root, bd=3, relief=RIDGE)
        frame.place(x=20, y=500, width=1300, height=180)

        scrolly = Scrollbar(frame, orient=VERTICAL)
        scrollx = Scrollbar(frame, orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 11), rowheight=25)
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))

        self.SupplierTable = ttk.Treeview(
        frame,
        columns=("supplier", "company", "phone", "email", "address", "gst"),
        xscrollcommand=scrollx.set,
        yscrollcommand=scrolly.set
    )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("supplier", text="Supplier Name")
        self.SupplierTable.heading("company", text="Company Name")
        self.SupplierTable.heading("phone", text="Phone")
        self.SupplierTable.heading("email", text="Email")
        self.SupplierTable.heading("address", text="Address")
        self.SupplierTable.heading("gst", text="GST Number")

        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("supplier", width=190)
        self.SupplierTable.column("company", width=190)
        self.SupplierTable.column("phone", width=170)
        self.SupplierTable.column("email", width=210)
        self.SupplierTable.column("address", width=330)
        self.SupplierTable.column("gst", width=190)

        self.SupplierTable.pack(fill=BOTH, expand=1)

        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.fetch_data()

    def fetch_data(self):
        try:
            self.db.execute("SELECT * FROM supplier")
            rows = self.db.fetchall()

            self.SupplierTable.delete(*self.SupplierTable.get_children())

            for row in rows:
                self.SupplierTable.insert(
                    "",
                    END,
                    values=(row[1], row[2], row[3], row[4], row[5], row[6])
                )

        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self.root)

    def get_data(self, ev):
        cursor_row = self.SupplierTable.focus()
        contents = self.SupplierTable.item(cursor_row)

        row = contents["values"]

        if row:
            self.var_supplier_name.set(row[0])
            self.var_company_name.set(row[1])
            self.var_phone.set(row[2])
            self.var_email.set(row[3])

            self.txt_address.delete("1.0", END)
            self.txt_address.insert(END, row[4])

            self.var_gst.set(row[5])

    def add(self):
        if self.var_supplier_name.get() == "":
            messagebox.showerror(
                "Error",
                "Supplier Name is required",
                parent=self.root
            )
            return

        try:
            address = self.txt_address.get("1.0", END).strip()

            self.db.execute(
                """
                INSERT INTO supplier
                (supplier_name, company_name, phone, email, address, gst_number)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    self.var_supplier_name.get(),
                    self.var_company_name.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    address,
                    self.var_gst.get()
                )
            )

            messagebox.showinfo(
                "Success",
                "Supplier Added Successfully",
                parent=self.root
            )
            self.fetch_data()
            self.clear()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e),
                parent=self.root
            )

    def clear(self):
        self.var_supplier_name.set("")
        self.var_company_name.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_gst.set("")
        self.var_search.set("")
        self.txt_address.delete("1.0", END)

    def search(self):
        if self.var_search.get() == "":
            messagebox.showerror(
                "Error",
                "Please enter Supplier Name to search",
                parent=self.root
            )
            return

        try:
            self.db.execute(
                "SELECT * FROM supplier WHERE supplier_name=%s",
                (self.var_search.get(),)
            )

            row = self.db.fetchone()

            if row is not None:
                self.var_supplier_name.set(row[1])
                self.var_company_name.set(row[2])
                self.var_phone.set(row[3])
                self.var_email.set(row[4])

                self.txt_address.delete("1.0", END)
                self.txt_address.insert(END, row[5])

                self.var_gst.set(row[6])

            else:
                messagebox.showerror(
                    "Error",
                    "No Record Found",
                    parent=self.root
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e),
                parent=self.root
            )



    def update(self):
        if self.var_supplier_name.get() == "":
            messagebox.showerror(
                "Error",
                "Please Search and Select a Supplier First",
                parent=self.root
            )
            return

        try:
            address = self.txt_address.get("1.0", END).strip()

            self.db.execute(
                """
                UPDATE supplier
                SET company_name=%s,
                    phone=%s,
                    email=%s,
                    address=%s,
                    gst_number=%s
                WHERE supplier_name=%s
                """,
                (
                    self.var_company_name.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    address,
                    self.var_gst.get(),
                    self.var_supplier_name.get()
                )
            )

            messagebox.showinfo(
                "Success",
                "Supplier Updated Successfully",
                parent=self.root
            )

            self.fetch_data()
            self.clear()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e),
                parent=self.root
            )

    def delete(self):
        if self.var_supplier_name.get() == "":
            messagebox.showerror(
                "Error",
                "Please Search and Select a Supplier First",
                parent=self.root
            )
            return

        confirm = messagebox.askyesno(
            "Confirm",
            "Do you really want to delete this supplier?",
            parent=self.root
        )

        if confirm:
            try:
                self.db.execute(
                    "DELETE FROM supplier WHERE supplier_name=%s",
                    (self.var_supplier_name.get(),)
                )

                messagebox.showinfo(
                    "Success",
                    "Supplier Deleted Successfully",
                    parent=self.root
                )
                self.fetch_data()
                self.clear()

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    str(e),
                    parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()