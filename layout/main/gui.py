from tkinter import CENTER, END, Frame, Label, PhotoImage, Scrollbar, messagebox, ttk, Button
from design.Entry import Entry
import mysql.connector as sql
import layout.auth.login as login
import layout.main.monitoring as moni

def get_details(email):
    global name, docid
    q = f'select  doctorId, doctorName from gait_db.tbldoctor where doctorEmail="{email}"'
    mycon = sql.connect(host='localhost', user='root',
                        passwd='', database='gait_db')
    cur = mycon.cursor()
    cur.execute(q)
    d = cur.fetchall()
    mycon.close()

    docid = d[0][0]
    name = d[0][1]


# ------------------------------------------------------- patient Query ------------------------------------------------------- #
def show_all(table):
    mycon = sql.connect(host='localhost', user='root',
                        passwd='', database='gait_db')
    cur = mycon.cursor()
    cur.execute(
        f'select * FROM gait_db.tblpatient where doctorId={docid}')
    all_jobs = cur.fetchall()
    mycon.close()
    i = 0
    for r in all_jobs:
        table.insert("", END, i, text="", values=(
            r[2], r[3], r[4], r[5], r[6], r[7]))
        i += 1

# ------------------------------------------------------- Insert patient ------------------------------------------------------- #
def create():
    global name, age, gender, weight, height, diagnose
    for widget in rt.winfo_children():
        widget.destroy()
    for widget in tab.winfo_children():
        widget.destroy()

    # Form
    # Labels
    name_l = Label(tab, text="Nama Pasien :", font=(
        'normal', 18, 'bold'), bg="#ECF2FF")
    name_l.grid(row=0, column=0, pady=10, padx=10)
    age_l = Label(tab, text="Umur :", font=(
        'normal', 18, 'bold'), bg="#ECF2FF")
    age_l.grid(row=1, column=0, pady=10, padx=10)
    gender_l = Label(tab, text="Jenis Kelamin :", font=(
        'normal', 18, 'bold'), bg="#ECF2FF")
    gender_l.grid(row=2, column=0, pady=10, padx=10)
    weight_l = Label(tab, text="Berat Badan :", font=(
        'normal', 18, 'bold'), bg="#ECF2FF")
    weight_l.grid(row=3, column=0, pady=10, padx=10)
    height_l = Label(tab, text="Tinggi Badan :", font=(
        'normal', 18, 'bold'), bg="#ECF2FF")
    height_l.grid(row=4, column=0, pady=10, padx=10)
    diagnose_l = Label(tab, text="Diagnosa Penyakit :", font=(
        'normal', 18, 'bold'), bg="#ECF2FF")
    diagnose_l.grid(row=5, column=0, pady=10, padx=10)

    # Entries
    style = ttk.Style(tab)
    style.configure("TCombobox", background="#ECF2FF",
                    foreground="#696969")

    name = Entry(tab, placeholder="Nama Pasien")
    name.grid(row=0, column=1, pady=10, padx=10)
    age = Entry(tab, placeholder="Umur Pasien")
    age.grid(row=1, column=1, pady=10, padx=10)
    
    gender = ttk.Combobox(tab, font=("normal", 18),
                        width=23, state='readonly')
    gender['values'] = ('Select', 'Laki-Laki', 'Perempuan')
    gender.current(0)
    gender.grid(row=2, column=1, pady=10, padx=10)
    weight = Entry(tab, placeholder="Berat Badan Pasien")
    weight.grid(row=3, column=1, pady=10, padx=10)
    height = Entry(tab, placeholder="Tinggi Badan Pasien")
    height.grid(row=4, column=1, pady=10, padx=10)
    diagnose = Entry(tab, placeholder="Diagnosa Penyakit Pasien")
    diagnose.grid(row=5, column=1, pady=10, padx=10)

    btn = Button(tab, text="Submit", font=(20), bg="#1e1e1e",
                fg="#FFFFFF", command=submit_patient)
    btn.grid(row=6, column=1, pady=10, padx=10)

# ------------------------------------------------------- Submit patient ------------------------------------------------------- #
def submit_patient():
    global name1, age1, gender1, weight1, height1, diagnose1
    name1 = name.get()
    age1 = age.get()
    gender1 = gender.get()
    weight1 = weight.get()
    height1 = height.get()
    diagnose1 = diagnose.get()
    print(name1, age1, gender1, weight1, height1, diagnose1)
    if name1 and age1 and gender1 and weight1 and height1 and diagnose1:
        if gender1 == "Select":
            messagebox.showinfo('ALERT!', 'Please provide Gender')
        else:
            exe1 = f'INSERT INTO gait_db.tblpatient(doctorId, patientName, patientAge, patientGender, patientWeight, patientHeight, patientMedic, CreationDate, UpdationDate) VALUES ("{docid}", "{name1}", "{age1}", "{gender1}", "{weight1}", "{height1}", "{diagnose1}", NULL, NULL)'
            try:
                mycon = sql.connect(host='localhost', user='root',
                                    passwd='', database='gait_db')
                cur = mycon.cursor()
                cur.execute(exe1)
                name.delete(0, END)
                age.delete(0, END)
                gender.delete(0, END)
                weight.delete(0, END)
                height.delete(0, END)
                diagnose.delete(0, END)
                mycon.commit()
                mycon.close()
                messagebox.showinfo('SUCCESS!', 'Berhasil Menambahkan Pasien Baru')
            except Exception as e:
                print(f"How exceptional! {e}")
                pass
    else:
        messagebox.showinfo('ALERT!', 'ALL FIELDS ARE MUST BE FILLED')

# ------------------------------------------------------- Display patients ------------------------------------------------------- #
def patient_list():
    for widget in rt.winfo_children():
        widget.destroy()
    for widget in tab.winfo_children():
        widget.destroy()

    scx = Scrollbar(tab, orient="horizontal")
    scy = Scrollbar(tab, orient="vertical")

    table = ttk.Treeview(tab, columns=( 'patientName', 'patientAge', 'patientGender', 'patientWeight', 'patientHeight', 'patientMedic'),
                        xscrollcommand=scx.set, yscrollcommand=scy.set)
    scx.pack(side="bottom", fill="x")
    scy.pack(side="right", fill="y")
    
    table.heading("patientName", text="Nama", anchor=CENTER)
    table.heading("patientAge", text="Umur", anchor=CENTER)
    table.heading("patientGender", text="Gender", anchor=CENTER)
    table.heading("patientWeight", text="Tinggi", anchor=CENTER)
    table.heading("patientHeight", text="Berat", anchor=CENTER)
    table.heading("patientMedic", text="Diagnosa", anchor=CENTER)

    table['show'] = 'headings'

    scx.config(command=table.xview)
    scy.config(command=table.yview)

    table.column("patientName", anchor=CENTER, width=150)
    table.column("patientAge", anchor=CENTER, width=50)
    table.column("patientGender", anchor=CENTER, width=50)
    table.column("patientWeight", anchor=CENTER, width=50)
    table.column("patientHeight", anchor=CENTER, width=50)
    table.column("patientMedic", anchor=CENTER, width=150)
    show_all(table)
    table.pack(fill="both", expand=1)

# ------------------------------------------------------- Monitoring ------------------------------------------------------- #
def open_mon(root):
    confirm = messagebox.askyesno(
        "Confirm Monitoring", "Do you really want to Open Monitoring?"
    )
    if confirm is True:
        bg.destroy()
        moni.mon_display(root)

# ------------------------------------------------------- Logout ------------------------------------------------------- #
def logout(root):
    confirm = messagebox.askyesno(
        "Confirm log-out", "Do you really want to log out?"
    )
    if confirm is True:
        bg.destroy()
        login.log(root)

# ------------------------------------------------------- Main Frame ------------------------------------------------------- #
def doct(root, email1):
    global email, bg
    email = email1
    
    bg = Frame(root, width=1050, height=700)
    bg.place(x=0, y=0)

    get_details(email)

    bg.load = PhotoImage(file='assets\\main_bgr.png')
    img = Label(root, image=bg.load)
    img.place(x=0, y=0)

    # Navbar
    ppf = Frame(root, width=50, height=50)
    ppf.load = PhotoImage(file="assets\\profile.png")
    pp = Label(root, image=ppf.load, bg="#1e1e1e")
    pp.place(x=800, y=25)
    
    nm = Label(root, text=f'{name}', font=(
        'normal', 12, 'bold'), bg="#1e1e1e", fg="#ECF2FF")
    nm.place(x=880, y=40)

    # Left
    lf = Frame(root, width=270, height=375, bg="#ECF2FF")
    lf.place(x=78, y=220)
    
    ip = Button(lf, text="Tambah Pasien", font=(
        # 'normal', 20), bg="#b32e2e", fg="#ECF2FF", command=lambda: print('add Clicked'))
        'normal', 20), bg="#b32e2e", fg="#ECF2FF", command=create)
    ip.grid(row=0, column=0, padx=40, pady=25)
    
    pl = Button(lf, text="Daftar Pasien", font=(
        # 'normal', 20), bg="#b32e2e", fg="#ECF2FF", command=lambda: print('list Clicked'))
        'normal', 20), bg="#b32e2e", fg="#ECF2FF", command=patient_list)
    pl.grid(row=1, column=0, padx=40, pady=25)
    
    pl = Button(lf, text="Monitoring", font=(
        # 'normal', 20), bg="#b32e2e", fg="#ECF2FF", command=lambda: print('cam Clicked'))
        'normal', 20), bg="#b32e2e", fg="#ECF2FF", command=lambda: open_mon(root))
    pl.grid(row=2, column=0, padx=40, pady=25)
    
    lgt = Button(lf, text="Keluar", font=(
        # 'normal', 20), bg="#b32e2e", fg="#ECF2FF", command=lambda: print('logout Clicked'))
        'normal', 20), bg="#b32e2e", fg="#ECF2FF", command=lambda: logout(root))
    lgt.grid(row=3, column=0, padx=40, pady=25)

    # Right
    global rt, tab
    rt = Frame(root, width=540, height=420, bg="#ECF2FF")
    rt.place(x=450, y=220)
    
    tab = Frame(root, bg="#ECF2FF")
    tab.place(x=450, y=200, width=540, height=460)
    