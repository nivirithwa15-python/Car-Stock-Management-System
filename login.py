from tkinter import *
from tkinter import messagebox
from register import RegisterClass
from db import Database
from dashboard import IMS

root = Tk()

root.title("Login System")
root.geometry("1350x700+0+0")
root.config(bg="white")
root.resizable(True,True)

title = Label(
    root,
    text="CAR SPARE PARTS - STOCK MANAGEMENT SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#0F4D7D",
    fg="white",
    padx=20,
    pady=10
)

title.pack(fill=X)
login_frame = Frame(
    root,
    bd=3,
    relief=RIDGE,
    bg="white"
)

login_frame.place(x=450, y=140, width=450, height=430)
lbl_login = Label(
    login_frame,
    text="USER LOGIN",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="#0F4D7D"
)

lbl_login.place(x=130, y=30)
# ========== Username ==========

lbl_user = Label(
    login_frame,
    text="Email",
    font=("Arial", 14),
    bg="white",
    fg="black"
)
lbl_user.place(x=40, y=100)

txt_user = Entry(
    login_frame,
    font=("Arial", 14),
    bg="lightyellow"
)
txt_user.place(x=40, y=130, width=360, height=35)
# ========== Password ==========

lbl_pass = Label(
    login_frame,
    text="Password",
    font=("Arial", 14),
    bg="white",
    fg="black"
)
lbl_pass.place(x=40, y=180)

txt_pass = Entry(
    login_frame,
    font=("Arial", 14),
    bg="lightyellow",
    show="*"
)
txt_pass.place(x=40, y=210, width=360, height=35)

def register_window():
    new_win = Toplevel(root)
    RegisterClass(new_win)

def login():
    db = Database()

    query = "SELECT * FROM employee WHERE email=%s AND password=%s"
    values = (
        txt_user.get(),
        txt_pass.get()
    )

    db.execute(query, values)
    row = db.fetchone()

    if row:
        messagebox.showinfo("Success", "Login Successful")

        root.destroy()

        main_root = Tk()
        obj = IMS(main_root)
        main_root.mainloop()

    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ========== Login Button ==========

btn_login = Button(
    login_frame,
    text="LOGIN",
    font=("Arial", 14, "bold"),
    bg="#0F4D7D",
    fg="white",
    cursor="hand2",
    command=login
)
btn_login.place(x=40, y=280, width=360, height=40)

# ========== Register Button ==========

btn_register = Button(
    login_frame,
    text="REGISTER",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    cursor="hand2",
command=register_window
)
btn_register.place(x=40, y=335, width=170, height=35)

# ========== Exit Button ==========

btn_exit = Button(
    login_frame,
    text="EXIT",
    font=("Arial", 12, "bold"),
    bg="#F44336",
    fg="white",
    cursor="hand2",
    command=root.destroy
)

btn_exit.place(x=230, y=335, width=170, height=35)

root.mainloop()