from tkinter import END, Frame, Label, PhotoImage, messagebox, Button

from design.Entry import Entry
import mysql.connector as sql
import layout.auth.login as login

def logi(root):
    try:
        r1.destroy()
    except Exception as e:
        print(f"Warning Found! {e}")
        pass
    login.log(root)

def doctors_registration(root):
    global r1, name, email, pwd, cpwd
    print("hello doctor")
    r1 = Frame(root, height=700, width=1050)
    r1.place(x=0, y=0)
    r1.render = PhotoImage(file="assets/bg_gait.png")
    img = Label(r1, image=r1.render)
    img.place(x=0, y=0)
    
    name_l = Label(r1, text="Name : ", bg='#1e1e1e', fg="#ECF2FF",
                font=('normal', 20, 'bold'))
    name_l.place(x=620, y=250)
    name = Entry(r1, placeholder='Enter Your Full Name...', width=20)
    name.place(x=720, y=250)
    
    email_l = Label(r1, text="Email : ", bg='#1e1e1e', fg="#ECF2FF",
                    font=('normal', 20, 'bold'))
    email_l.place(x=620, y=300)
    email = Entry(r1, placeholder='Email', width=20)
    email.place(x=720, y=300)

    pwd_l = Label(r1, text="Password : ", bg='#1e1e1e', fg="#ECF2FF",
                font=('normal', 20, 'bold'))
    pwd_l.place(x=565, y=350)
    pwd = Entry(r1, placeholder='Password', show="*", width=20)
    pwd.place(x=720, y=350)

    con_pwd_l = Label(r1, text="Confirm : ", bg='#1e1e1e', fg="#ECF2FF",
                    font=('normal', 20, 'bold'))
    con_pwd_l.place(x=585, y=400)
    cpwd = Entry(r1, placeholder='Confirm Password', show="*", width=20)
    cpwd.place(x=720, y=400)

    r1.back = PhotoImage(file="assets\\back_btn.png")
    btn = Button(r1, image=r1.back, bg='#1e1e1e',
                bd=0, activebackground="#1e1e1e", command=lambda: logi(root))
    btn.place(x=620, y=450)
    
    r1.bn = PhotoImage(file="assets\\reg_btn.png")
    btn = Button(r1, image=r1.bn, bg='#1e1e1e', bd=0,
                activebackground="#1e1e1e", command=lambda: doctors_account_check(root))
    btn.place(x=820, y=450)

def doctors_account_check(root):
    global name1, email1, pwd1, cpwd1
    name1 = name.get()
    email1 = email.get()
    pwd1 = pwd.get()
    cpwd1 = cpwd.get()
    print(name1, email1, pwd1, cpwd1)
    if name1 and email1 and pwd1 and cpwd1:
        mycon = sql.connect(host='localhost', user='root',
                            passwd='', database='gait_db')
        cur = mycon.cursor()
        cur.execute('select doctorEmail from tbldoctor')
        total = cur.fetchall()
        mycon.close()
        exist_email = []
        for i in total:
            exist_email.append(i[0])
        print("existing doctor account:", exist_email)

        if email1 in exist_email:
            messagebox.showinfo('ALERT!', 'EMAIL ALREADY REGISTERED')
            email.delete(0, END)

        else:
            if pwd1 == cpwd1:
                doctors_submit_form(root)
            else:
                messagebox.showinfo('ALERT!', 'PASSWORDS DO NOT MATCH')

    else:
        messagebox.showinfo('ALERT!', 'ALL FIELDS ARE MUST BE FILLED')

def doctors_submit_form(root):

    print(name1, email1)
    # create_folder()
    
    # unfinished details in username DB
    exe = f'insert into tbldoctor values(null,"{name1}","{email1}",null,"{pwd1}",null,null)'
    
    try:
        mycon = sql.connect(host='localhost', user='root',
                            passwd='', database='gait_db')
        cur = mycon.cursor()
        cur.execute(exe)
        name.delete(0, END)
        email.delete(0, END)
        pwd.delete(0, END)
        cpwd.delete(0, END)
        mycon.commit()
        mycon.close()
        messagebox.showinfo('SUCCESS!', 'Registration Successful')
        logi(root)
    except Exception as e:
        print(f"Warning Found! {e}")
        pass
