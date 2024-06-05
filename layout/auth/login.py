from tkinter import Frame, Label, PhotoImage, messagebox, Button
from design.Entry import Entry
import mysql.connector as sql
from layout.auth.register import doctors_registration
from layout.main.gui import doct

def success(root, email1):
    f1.destroy()
    try:
        r1.destroy()  # type: ignore # noqa: F821
    except Exception as e:
        print(f"Warning Found! {e}")
        pass

    s = f'select doctorId from tbldoctor where doctorEmail="{email1}"'
    mycon = sql.connect(host='localhost', user='root',
                        passwd='', database='gait_db')
    cur = mycon.cursor()
    cur.execute(s)
    q = cur.fetchall()
    mycon.close()
    print(q)
    doct(root, email1)


def submit(root):
    mycon = sql.connect(host='localhost', user='root',
                        passwd='', database='gait_db')
    cur = mycon.cursor()
    cur.execute('select doctorEmail, doctorpassword from tbldoctor')
    total = cur.fetchall()
    mycon.close()
    email1 = email.get()
    password = pwd.get()
    if email1 and password:
        for i in total:
            if email1 == i[0] and password == i[1]:
                return success(root, email1)
            elif email1 == i[0] and password != i[1]:
                messagebox.showinfo('Alert!', 'Invalid Credentials')
                break
        else:
            messagebox.showinfo(
                'Alert!', 'Email is not registered, Please register')
    else:
        messagebox.showinfo(
            'Alert!', 'Please Enter both Email and Password')


def reg(root):
    try:
        f1.destroy()
    except Exception as e:
        print(f"Warning Found! {e}")
        pass
    doctors_registration(root)


def log(root):
    global f1, email, pwd
    try:
        f2.destroy()  # type: ignore # noqa: F821
    except Exception as e:
        print(f"Warning Found! {e}")
        pass
    f1 = Frame(root, width=1050, height=700, bg='#1e1e1e')
    f1.place(x=0, y=0)

    # Background
    f1.render = PhotoImage(file='assets\\bg_gait.png')
    img = Label(f1, image=f1.render)
    img.place(x=0, y=0)

    # Email
    email_l = Label(f1, text="Email : ", bg='#1e1e1e',
                    font=('normal', 20, 'bold'), fg="#ECF2FF")
    email_l.place(x=620, y=300)
    email = Entry(f1, width=24, placeholder="Enter your Email..")
    email.place(x=720, y=300)

    # Password
    pwd_l = Label(f1, text="Password : ", bg='#1e1e1e',
                font=('normal', 20, 'bold'), fg="#ECF2FF")
    pwd_l.place(x=565, y=350)
    pwd = Entry(f1, show="*", width=24, placeholder="Enter your Password..")
    pwd.place(x=720, y=350)

    # Buttons
    f1.bn = PhotoImage(file="assets\\login_btn.png")
    btn = Button(f1, image=f1.bn, bg='#1e1e1e', bd=0,
                activebackground="#1e1e1e", command=lambda: submit(root))
    btn.place(x=820, y=420)

    f1.bn1 = PhotoImage(file="assets\\reg_btn.png")
    btn1 = Button(f1, image=f1.bn1, bg='#1e1e1e', bd=0,
                activebackground="#1e1e1e", command=lambda: reg(root))
    btn1.place(x=620, y=420)
