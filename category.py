from tkinter import *
from tkinter import ttk,messagebox
from db import Database


class CategoryClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x800+220+30")
        self.root.title("Category Details")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = Database()

        # ================= Variables =================

        self.var_category = StringVar()

        # ================= Search Variables =================

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        # ================= Title =================

        title = Label(
            self.root,
            text="Manage Category Details",
            font=("Arial", 20, "bold"),
            bg="#0f4d7d",
            fg="white"
        )
        title.pack(side=TOP, fill=X)

        SearchFrame = LabelFrame(
            self.root,
            text="Search Category",
            font=("Arial", 12, "bold"),
            bg="white"
        )
        SearchFrame.place(x=750, y=60, width=330, height=80)

        cmb_search = ttk.Combobox(
            SearchFrame,
            textvariable=self.var_searchby,
            values=("Select", "Category"),
            state="readonly",
            justify=CENTER,
            font=("Arial", 12)
        )
        cmb_search.place(x=10, y=10, width=100)
        cmb_search.current(0)

        txt_search = Entry(
            SearchFrame,
            textvariable=self.var_searchtxt,
            font=("Arial", 12),
            bg="lightyellow"
        )
        txt_search.place(x=120, y=10, width=100)

        btn_search = Button(
            SearchFrame,
            text="Search",
            command=self.search,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        )
        btn_search.place(x=230, y=8, width=80, height=28)

        # ================= Labels =================

        lbl_category = Label(
            self.root,
            text="Category Name",
            font=("Arial", 15),
            bg="white"
        )
        lbl_category.place(x=60, y=100)

        lbl_desc = Label(
            self.root,
            text="Description",
            font=("Arial", 15),
            bg="white"
        )
        lbl_desc.place(x=60, y=180)

        # ================= Entry =================

        txt_category = Entry(
            self.root,
            textvariable=self.var_category,
            font=("Arial", 15),
            bg="lightyellow"
        )
        txt_category.place(x=240, y=100, width=320)

        self.txt_desc = Text(
            self.root,
            font=("Arial", 15),
            bg="lightyellow"
        )
        self.txt_desc.place(x=240, y=180, width=350, height=150)

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
        btn_save.place(x=750, y=150, width=180, height=30)

        btn_update = Button(
            self.root,
            text="Update",
            command=self.update,
            font=("Arial", 14, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        btn_update.place(x=750, y=190, width=180, height=30)

        btn_delete = Button(
            self.root,
            text="Delete",
            command=self.delete,
            font=("Arial", 14, "bold"),
            bg="#F44336",
            fg="white",
            cursor="hand2"
        )
        btn_delete.place(x=750, y=230, width=180, height=30)

        btn_clear = Button(
            self.root,
            text="Clear",
            command=self.clear,
            font=("Arial", 14, "bold"),
            bg="#607D8B",
            fg="white",
            cursor="hand2"
        )
        btn_clear.place(x=750, y=270, width=180, height=30)

        # ================= Category Details =================

        detailsFrame = Frame(self.root, bd=3, relief=RIDGE)
        detailsFrame.place(x=20, y=400, width=1050, height=280)

        scrolly = Scrollbar(detailsFrame, orient=VERTICAL)

        self.CategoryTable = ttk.Treeview(
            detailsFrame,
            columns=("cid", "category", "description"),
            yscrollcommand=scrolly.set
        )

        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading(
            "cid",
            text="Category ID"
        )

        self.CategoryTable.heading(
            "category",
            text="Category Name"
        )

        self.CategoryTable.heading(
            "description",
            text="Description"
        )

        self.CategoryTable["show"] = "headings"

        self.CategoryTable.column(
            "cid",
            width=100,
            anchor=CENTER,
            stretch=True
        )

        self.CategoryTable.column(
            "category",
            width=280,
            anchor=W,
            stretch=True
        )

        self.CategoryTable.column(
            "description",
            width=620,
            anchor=W,
            stretch=True
        )

        self.CategoryTable.pack(
            fill=BOTH,
            expand=1
        )

        self.fetch_data()

        self.CategoryTable.bind(
            "<ButtonRelease-1>",
            self.get_data
        )

        self.fetch_data()
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)

    def add(self):
            if self.var_category.get() == "":
                messagebox.showerror(
                    "Error",
                    "Category Name is required",
                    parent=self.root
                )
                return

            try:
                desc = self.txt_desc.get("1.0", END).strip()

                self.db.execute(
                    "INSERT INTO category (category_name, description) VALUES (%s,%s)",
                    (
                        self.var_category.get(),
                        desc
                    )
                )

                messagebox.showinfo(
                    "Success",
                    "Category Added Successfully",
                    parent=self.root
                )

                self.fetch_data()
                self.clear()

                self.var_category.set("")
                self.txt_desc.delete("1.0", END)
                self.fetch_data()

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    str(e),
                    parent=self.root
                )

    def clear(self):
        self.var_category.set("")
        self.txt_desc.delete("1.0", END)

    def fetch_data(self):
        try:
            self.db.execute(
                "SELECT category_id, category_name, description FROM category"
            )

            rows = self.db.fetchall()

            self.CategoryTable.delete(*self.CategoryTable.get_children())

            for row in rows:
                self.CategoryTable.insert("", END, values=row)

        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self.root)

    def get_data(self, ev):
            f = self.CategoryTable.focus()
            content = self.CategoryTable.item(f)

            row = content["values"]

            if row:
                self.var_category.set(row[1])

                self.txt_desc.delete("1.0", END)
                self.txt_desc.insert(END, row[2])

    def update(self):
            if self.var_category.get() == "":
                messagebox.showerror(
                    "Error",
                    "Category Name is required",
                    parent=self.root
                )
                return

            try:
                desc = self.txt_desc.get("1.0", END).strip()

                self.db.execute(
                    "UPDATE category SET description=%s WHERE category_name=%s",
                    (
                        desc,
                        self.var_category.get()
                    )
                )

                messagebox.showinfo(
                    "Success",
                    "Category Updated Successfully",
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
        if self.var_category.get() == "":
            messagebox.showerror(
                "Error",
                "Select a category from the table",
                parent=self.root
            )
            return
        try:
            op = messagebox.askyesno(
                "Confirm",
                "Do you really want to delete this category?",
                parent=self.root
            )

            if op:
                self.db.execute(
                    "DELETE FROM category WHERE category_name=%s",
                    (self.var_category.get(),)
                )

                messagebox.showinfo(
                    "Success",
                    "Category Deleted Successfully",
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

    def search(self):
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror(
                    "Error",
                    "Select Search By option",
                    parent=self.root
                )
                return

            if self.var_searchtxt.get() == "":
                messagebox.showerror(
                    "Error",
                    "Search text is required",
                    parent=self.root
                )
                return

            self.db.execute(
                "SELECT category_id, category_name, description FROM category WHERE category_name LIKE %s",
                ("%" + self.var_searchtxt.get() + "%",)
            )

            rows = self.db.fetchall()

            self.CategoryTable.delete(*self.CategoryTable.get_children())

            for row in rows:
                self.CategoryTable.insert("", END, values=row)

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e),
                parent=self.root
            )
if __name__ == "__main__":
    root = Tk()
    obj = CategoryClass(root)
    root.mainloop()