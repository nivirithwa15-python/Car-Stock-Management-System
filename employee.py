from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db import Database


class EmployeeClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+180+80")
        self.root.title("Employee Details")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = Database()

        # ================= Variables =================

        self.var_emp_id = StringVar()
        self.var_old_emp_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_password = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        self.var_search = StringVar()

        # ================= Title =================

        title = Label(
            self.root,
            text="Manage Employee Details",
            font=("Arial", 20, "bold"),
            bg="#0f4d7d",
            fg="white"
        )
        title.pack(side=TOP, fill=X)

        # ================= Labels =================

        Label(
            self.root,
            text="Employee ID",
            font=("Arial", 15),
            bg="white"
        ).place(x=40, y=70)

        Label(
            self.root,
            text="Employee Name",
            font=("Arial", 15),
            bg="white"
        ).place(x=40, y=120)

        Label(
            self.root,
            text="Email",
            font=("Arial", 15),
            bg="white"
        ).place(x=40, y=170)

        Label(
            self.root,
            text="Gender",
            font=("Arial", 15),
            bg="white"
        ).place(x=40, y=220)

        Label(
            self.root,
            text="Contact",
            font=("Arial", 15),
            bg="white"
        ).place(x=40, y=270)

        Label(
            self.root,
            text="DOB",
            font=("Arial", 15),
            bg="white"
        ).place(x=40, y=320)

        Label(
            self.root,
            text="DOJ",
            font=("Arial", 15),
            bg="white"
        ).place(x=40, y=370)

        Label(
            self.root,
            text="Password",
            font=("Arial", 15),
            bg="white"
        ).place(x=600, y=70)

        Label(
            self.root,
            text="User Type",
            font=("Arial", 15),
            bg="white"
        ).place(x=600, y=120)

        Label(
            self.root,
            text="Salary",
            font=("Arial", 15),
            bg="white"
        ).place(x=600, y=170)

        # ================= Entry Fields =================

        Entry(
            self.root,
            textvariable=self.var_emp_id,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=220, y=70, width=250)

        Entry(
            self.root,
            textvariable=self.var_name,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=220, y=120, width=250)

        Entry(
            self.root,
            textvariable=self.var_email,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=220, y=170, width=250)

        cmb_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            values=("Male", "Female", "Other"),
            state="readonly",
            justify=CENTER,
            font=("Arial", 14)
        )
        cmb_gender.place(x=220, y=220, width=250)
        cmb_gender.current(0)

        Entry(
            self.root,
            textvariable=self.var_contact,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=220, y=270, width=250)

        Entry(
            self.root,
            textvariable=self.var_dob,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=220, y=320, width=250)

        Entry(
            self.root,
            textvariable=self.var_doj,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=220, y=370, width=250)

        Entry(
            self.root,
            textvariable=self.var_password,
            show="*",
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=760, y=70, width=250)

        cmb_utype = ttk.Combobox(
            self.root,
            textvariable=self.var_utype,
            values=("Admin", "Employee"),
            state="readonly",
            justify=CENTER,
            font=("Arial", 14)
        )
        cmb_utype.place(x=760, y=120, width=250)
        cmb_utype.current(1)

        Entry(
            self.root,
            textvariable=self.var_salary,
            font=("Arial", 15),
            bg="lightyellow"
        ).place(x=760, y=170, width=250)

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
        btn_save.place(x=600, y=260, width=150, height=40)

        btn_update = Button(
            self.root,
            text="Update",
            command=self.update,
            font=("Arial", 14, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        btn_update.place(x=780, y=260, width=150, height=40)

        btn_delete = Button(
            self.root,
            text="Delete",
            command=self.delete,
            font=("Arial", 14, "bold"),
            bg="#F44336",
            fg="white",
            cursor="hand2"
        )
        btn_delete.place(x=600, y=320, width=150, height=40)

        btn_clear = Button(
            self.root,
            text="Clear",
            command=self.clear,
            font=("Arial", 14, "bold"),
            bg="#607D8B",
            fg="white",
            cursor="hand2"
        )
        btn_clear.place(x=780, y=320, width=150, height=40)

        # ================= Search =================

        Label(
            self.root,
            text="Search (Employee ID)",
            font=("Arial", 14),
            bg="white"
        ).place(x=40, y=440)

        Entry(
            self.root,
            textvariable=self.var_search,
            font=("Arial", 14),
            bg="lightyellow"
        ).place(x=230, y=440, width=220)

        Button(
            self.root,
            text="Search",
            command=self.search,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        ).place(x=470, y=438, width=120, height=32)

        # ================= Employee Table =================

        frame = Frame(self.root, bd=3, relief=RIDGE)
        frame.place(x=20, y=490, width=1150, height=180)

        scrolly = Scrollbar(frame, orient=VERTICAL)
        scrollx = Scrollbar(frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(
            frame,
            columns=(
                "emp_id",
                "name",
                "email",
                "gender",
                "contact",
                "dob",
                "doj",
                "password",
                "utype",
                "salary"
            ),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("emp_id", text="Employee ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="DOB")
        self.EmployeeTable.heading("doj", text="DOJ")
        self.EmployeeTable.heading("password", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("emp_id", width=100)
        self.EmployeeTable.column("name", width=140)
        self.EmployeeTable.column("email", width=180)
        self.EmployeeTable.column("gender", width=80)
        self.EmployeeTable.column("contact", width=110)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("password", width=120)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("salary", width=100)

        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.fetch_data()

    def fetch_data(self):
        try:
            self.db.execute("SELECT * FROM employee")
            rows = self.db.fetchall()

            self.EmployeeTable.delete(*self.EmployeeTable.get_children())

            for row in rows:
                self.EmployeeTable.insert(
                    "",
                    END,
                    values=(
                        row[0],   # emp_id
                        row[1],   # name
                        row[2],   # email
                        row[3],   # gender
                        row[4],   # contact
                        row[5],   # dob
                        row[6],   # doj
                        row[7],   # password
                        row[8],   # utype
                        row[9]    # salary
                    )
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e),
                parent=self.root
            )

    def get_data(self, ev):
        cursor_row = self.EmployeeTable.focus()
        contents = self.EmployeeTable.item(cursor_row)

        row = contents["values"]

        if row:
            self.var_emp_id.set(row[0])
            self.var_old_emp_id.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_contact.set(row[4])
            self.var_dob.set(row[5])
            self.var_doj.set(row[6])
            self.var_password.set(row[7])
            self.var_utype.set(row[8])
            self.var_salary.set(row[9])

    def add(self):
        if (
            self.var_emp_id.get() == "" or
            self.var_name.get() == "" or
            self.var_email.get() == "" or
            self.var_password.get() == ""
        ):
            messagebox.showerror(
                "Error",
                "Employee ID, Name, Email and Password are required",
                parent=self.root
            )
            return

        try:
            self.db.execute(
                "SELECT * FROM employee WHERE emp_id=%s OR email=%s",
                (
                    self.var_emp_id.get(),
                    self.var_email.get()
                )
            )

            row = self.db.fetchone()

            if row is not None:
                messagebox.showerror(
                    "Error",
                    "Employee ID or Email already exists",
                    parent=self.root
                )
                return

            self.db.execute(
                """
                INSERT INTO employee
                (
                    emp_id,
                    name,
                    email,
                    gender,
                    contact,
                    dob,
                    doj,
                    password,
                    utype,
                    salary
                )
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    self.var_emp_id.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_contact.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_password.get(),
                    self.var_utype.get(),
                    self.var_salary.get()
                )
            )

            messagebox.showinfo(
                "Success",
                "Employee Added Successfully",
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

    def update(self):
        if self.var_old_emp_id.get() == "":
            messagebox.showerror(
                "Error",
                "Please Select an Employee First",
                parent=self.root
            )
            return

        if self.var_emp_id.get() == "":
            messagebox.showerror(
                "Error",
                "Employee ID is required",
                parent=self.root
            )
            return

        try:
            # Check whether the new Employee ID already exists
            if self.var_emp_id.get() != self.var_old_emp_id.get():

                self.db.execute(
                    "SELECT * FROM employee WHERE emp_id=%s",
                    (self.var_emp_id.get(),)
                )

                existing = self.db.fetchone()

                if existing is not None:
                    messagebox.showerror(
                        "Error",
                        "New Employee ID already exists",
                        parent=self.root
                    )
                    return

            # Update employee details
            self.db.execute(
                """
                UPDATE employee
                SET
                    emp_id=%s,
                    name=%s,
                    email=%s,
                    gender=%s,
                    contact=%s,
                    dob=%s,
                    doj=%s,
                    password=%s,
                    utype=%s,
                    salary=%s
                WHERE emp_id=%s
                """,
                (
                    self.var_emp_id.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_contact.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_password.get(),
                    self.var_utype.get(),
                    self.var_salary.get(),
                    self.var_old_emp_id.get()
                )
            )

            messagebox.showinfo(
                "Success",
                "Employee Updated Successfully",
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
        if self.var_emp_id.get() == "":
            messagebox.showerror(
                "Error",
                "Please Select an Employee First",
                parent=self.root
            )
            return

        confirm = messagebox.askyesno(
            "Confirm",
            "Do you really want to delete this employee?",
            parent=self.root
        )

        if confirm:
            try:
                self.db.execute(
                    "DELETE FROM employee WHERE emp_id=%s",
                    (self.var_emp_id.get(),)
                )

                messagebox.showinfo(
                    "Success",
                    "Employee Deleted Successfully",
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
        if self.var_search.get() == "":
            messagebox.showerror(
                "Error",
                "Please enter Employee ID to search",
                parent=self.root
            )
            return

        try:
            self.db.execute(
                "SELECT * FROM employee WHERE emp_id=%s",
                (self.var_search.get(),)
            )

            row = self.db.fetchone()

            if row is not None:
                self.var_emp_id.set(row[0])
                self.var_old_emp_id.set(row[0])
                self.var_name.set(row[1])
                self.var_email.set(row[2])
                self.var_gender.set(row[3])
                self.var_contact.set(row[4])
                self.var_dob.set(str(row[5]))
                self.var_doj.set(str(row[6]))
                self.var_password.set(row[7])
                self.var_utype.set(row[8])
                self.var_salary.set(row[9])

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
                parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_old_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Male")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_password.set("")
        self.var_utype.set("Employee")
        self.var_salary.set("")
        self.var_search.set("")

        self.fetch_data()

if __name__ == "__main__":
    root = Tk()
    obj = EmployeeClass(root)
    root.mainloop()
