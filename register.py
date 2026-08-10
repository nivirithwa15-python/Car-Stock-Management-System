from tkinter import *
from tkinter import ttk, messagebox
from db import Database


class RegisterClass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+220+130")
        self.root.title("User Registration")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = Database()

        # ================= Variables =================
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        self.var_contact = StringVar()
        self.var_utype = StringVar()

        # ================= Title =================
        title = Label(
            self.root,
            text="User Registration",
            font=("goudy old style", 20, "bold"),
            bg="#0f4d7d",
            fg="white"
        )
        title.pack(side=TOP, fill=X)

        # ================= Labels & Entries =================

        lbl_name = Label(
            self.root,
            text="Name",
            font=("goudy old style", 15),
            bg="white"
        )
        lbl_name.place(x=50, y=80)

        txt_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 15),
            bg="lightyellow"
        )
        txt_name.place(x=180, y=80, width=300)

        lbl_email = Label(
            self.root,
            text="Email",
            font=("goudy old style", 15),
            bg="white"
        )
        lbl_email.place(x=50, y=140)

        txt_email = Entry(
            self.root,
            textvariable=self.var_email,
            font=("goudy old style", 15),
            bg="lightyellow"
        )
        txt_email.place(x=180, y=140, width=300)

        lbl_contact = Label(
            self.root,
            text="Contact",
            font=("goudy old style", 15),
            bg="white"
        )
        lbl_contact.place(x=50, y=200)

        txt_contact = Entry(
            self.root,
            textvariable=self.var_contact,
            font=("goudy old style", 15),
            bg="lightyellow"
        )
        txt_contact.place(x=180, y=200, width=300)

        lbl_password = Label(
            self.root,
            text="Password",
            font=("goudy old style", 15),
            bg="white"
        )
        lbl_password.place(x=550, y=80)

        txt_password = Entry(
            self.root,
            textvariable=self.var_password,
            font=("goudy old style", 15),
            bg="lightyellow",
            show="*"
        )
        txt_password.place(x=720, y=80, width=300)

        lbl_cpassword = Label(
            self.root,
            text="Confirm Password",
            font=("goudy old style", 15),
            bg="white"
        )
        lbl_cpassword.place(x=550, y=140)

        txt_cpassword = Entry(
            self.root,
            textvariable=self.var_cpassword,
            font=("goudy old style", 15),
            bg="lightyellow",
            show="*"
        )
        txt_cpassword.place(x=720, y=140, width=300)

        lbl_utype = Label(
            self.root,
            text="User Type",
            font=("goudy old style", 15),
            bg="white"
        )
        lbl_utype.place(x=550, y=200)

        cmb_utype = ttk.Combobox(
            self.root,
            textvariable=self.var_utype,
            values=("Admin", "Employee"),
            state="readonly",
            justify=CENTER,
            font=("goudy old style", 15)
        )
        cmb_utype.place(x=720, y=200, width=300)
        cmb_utype.current(0)

        # ================= Buttons =================

        btn_save = Button(
            self.root,
            text="Save",
            command=self.add,
            font=("goudy old style", 15, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2"
        )
        btn_save.place(x=180, y=300, width=120, height=35)

        btn_update = Button(
            self.root,
            text="Update",
            command=self.update,
            font=("goudy old style", 15, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2"
        )
        btn_update.place(x=330, y=300, width=120, height=35)

        btn_delete = Button(
            self.root,
            text="Delete",
            command=self.delete,
            font=("goudy old style", 15, "bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2"
        )
        btn_delete.place(x=480, y=300, width=120, height=35)

        btn_clear = Button(
            self.root,
            text="Clear",
            command=self.clear,
            font=("goudy old style", 15, "bold"),
            bg="#607d8b",
            fg="white",
            cursor="hand2"
        )
        btn_clear.place(x=630, y=300, width=120, height=35)


        # ================= Employee Details =================

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=20, y=370, width=1050, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(
            emp_frame,
            columns=("emp_id", "name", "email", "contact", "user_type"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("emp_id", text="ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("user_type", text="User Type")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("emp_id", width=60)
        self.EmployeeTable.column("name", width=180)
        self.EmployeeTable.column("email", width=250)
        self.EmployeeTable.column("contact", width=150)
        self.EmployeeTable.column("user_type", width=120)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        # ================= Functions =================

    def add(self):
        # Empty field validation
        if (
                self.var_name.get() == "" or
                self.var_email.get() == "" or
                self.var_contact.get() == "" or
                self.var_password.get() == "" or
                self.var_cpassword.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            return

        # Password validation
        if self.var_password.get() != self.var_cpassword.get():
            messagebox.showerror(
                "Error",
                "Password and Confirm Password should be same",
                parent=self.root
            )
            return

        # Check if email already exists
        query = "SELECT * FROM employee WHERE email=%s"
        self.db.execute(query, (self.var_email.get(),))

        row = self.db.fetchone()

        if row:
           messagebox.showerror(
          "Error",
      "Email already exists. Please use another email.",
               parent=self.root
                )
           return

        # Insert employee data
        query = """
        INSERT INTO employee (emp_id,name, email, password, contact, utype)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        emp_id = "EMP" + self.var_contact.get()[-4:]

        values = (
            emp_id,
            self.var_name.get(),
            self.var_email.get(),
            self.var_password.get(),
            self.var_contact.get(),
            self.var_utype.get()
        )

        success = self.db.execute(query, values)

        if success:
            messagebox.showinfo(
                "Success",
                "Employee Registered Successfully",
                parent=self.root
            )
        else:
            messagebox.showerror(
                "Error",
                "Registration Failed",
                parent=self.root
            )
            return

        self.clear()

    def update(self):
        messagebox.showinfo("Update", "Update function will be added later")

    def delete(self):
        messagebox.showinfo("Delete", "Delete function will be added later")

    def clear(self):
        self.var_name.set("")
        self.var_email.set("")
        self.var_password.set("")
        self.var_cpassword.set("")
        self.var_contact.set("")
        self.var_utype.set("Admin")

