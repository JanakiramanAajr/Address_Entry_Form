# import
import mysql.connector as sql
from tkinter import *
# Connect DataBase
mydb = sql.connect(
    host="localhost",
    user="root",
    password="",
)
mycursor = mydb.cursor(buffered=True)
try:
    mycursor.execute("CREATE DATABASE Address_Entry_Form")
except:
    pass
mycursor.execute("USE Address_Entry_Form")
# mycursor.execute("DROP TABLE Data",)
try:
    mycursor.execute("CREATE TABLE Data(First_name varchar(50), Last_name varchar(50), Aadhar_No varchar(50), Address varchar(50),Pincode varchar(50), Mobile varchar(50))")
except:
    pass
# mycursor.execute("INSERT TABLE Data(First_name varchar(50), Last_name varchar(50), Aadhar_No varchar(50), Address varchar(50),Pincode varchar(50), Mobile varchar(50))")
# Variables
font = ('Arial', 15)
# Main Window
window = Tk()
window.title('Address Entry Form')
#  Submit function
def click():
    mycursor.execute("INSERT INTO Data VALUES(%s,%s,%s,%s,%s,%s )",(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent6.get()))
    mydb.commit()
    for j in ent:
        j.delete(0,END)
# clear function
def clear_it():
    for j in ent:
        j.delete(0,END)
def clr():
    enta.delete(0, END)
def search():
    window1 = Tk()
    window1.title('Address Entry Form')
    global enta
    def submit():
        li = []
        mycursor.execute("SELECT * FROM Data")
        Datas = mycursor.fetchall()
        for data in Datas:
            if enta.get() in data:
                li.append(list(data))
        for ind_no0,li1 in enumerate(li):
            for ind_no1, text1 in enumerate(li1):

                lbl_data = f'{labels[ind_no1]} { text1}'
                lbl2 = Label(master=frm_form1, text=lbl_data, font=font,relief=RAISED,width=20)
                lbl2.grid(column=ind_no0, row=ind_no1+2, sticky='e')
    frm_form1 = Frame(master=window1, relief=SUNKEN, borderwidth=10)
    frm_form1.pack()
    lbl1 = Label(master=frm_form1, text='Enter the First Name', font=font)
    lbl1.grid(column=0, row=0, sticky='e')
    enta = Entry(master=frm_form1, font=font, width=20,relief=SUNKEN)
    enta.grid(column=1, row=1)
    btn1_submit = Button(master=window1, text='Submit', command=submit)
    btn1_submit.pack(side=RIGHT, padx=10, pady=10)
    btn1_clr = Button(master=window1, text='Clear', command=clr)
    btn1_clr.pack(side=RIGHT, padx=10, pady=10)
    window1.mainloop()
# Form Frame
frm_form = Frame(master=window, relief=SUNKEN, borderwidth=10)
frm_form.pack()
# Fields
labels = ['First Name:', 'Last Name:', 'Aadhar No:', 'Address:', 'Pincode:', 'Mobile:']
for ind_no, text in enumerate(labels):
    lbl = Label(master=frm_form, text=text, font=font)
    lbl.grid(column=0, row=ind_no, sticky='e')
ent1 = Entry(master=frm_form, font=font, width=40,relief=SUNKEN)
ent1.grid(column=1, row=0)
ent2 = Entry(master=frm_form, font=font, width=40,relief=SUNKEN)
ent2.grid(column=1, row=1)
ent3 = Entry(master=frm_form, font=font, width=40,relief=SUNKEN)
ent3.grid(column=1, row=2)
ent4 = Entry(master=frm_form, font=font, width=40,relief=SUNKEN)
ent4.grid(column=1, row=3)
ent5 = Entry(master=frm_form, font=font, width=40,relief=SUNKEN)
ent5.grid(column=1, row=4)
ent6 = Entry(master=frm_form, font=font, width=40,relief=SUNKEN)
ent6.grid(column=1, row=5)
ent=[ent1,ent2,ent3,ent4,ent5,ent6]
frm_form.pack()
# Button
btn_submit = Button(master=window, text='Submit', command=click)
btn_clear = Button(master=window, text='Clear', command= clear_it)
btn_open = Button(master=window, text='Search',command=search)
btn_submit.pack(side=RIGHT, padx=10, pady=10)
btn_clear.pack(side=RIGHT, padx=10, pady=10)
btn_open.pack(side=LEFT, padx=10, pady=10)
window.mainloop()