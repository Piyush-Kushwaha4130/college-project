from tkinter import *
from tkinter import ttk
import mysql.connector as connector
from PIL import Image, ImageTk
import tkinter.messagebox

conn = connector.connect(user = "root" ,host = "localhost",  password = "Code@1234", database = "college_student")

root = tkinter.Tk()

cur = conn.cursor()
def insert():
    admi_no = admi_noentry.get()
    name = nameentry.get()
    father_name = father_nameentry.get()
    gen = genentry.get()
    categ = categentry.get()
    branch = branchentry.get()
    year = yearentry.get()
    cont= contentry.get()
    addr= addrentry.get()

    query = "INSERT INTO college_stu_sys(admission_no, student_name, father_name, gender, Category, branch, year, contact_no, address ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    e1 = (admi_no, name, father_name, gen, categ, branch, year, cont, addr)
    cur.execute(query, e1)
    conn.commit()
    tkinter.messagebox.showinfo(" ","Added Successfully")

def reset():
    admi_no.set("")
    name.set("")
    father_name.set("")
    gen.set("")
    categ.set("")
    branch.set("")
    year.set("")
    cont.set("")
    addr.set("")
    
def delete():
    admi_no = admi_noentry.get()
    query = f"DELETE FROM college_stu_sys WHERE admission_no= {admi_no}"
    cur.execute(query)
    conn.commit()
    tkinter.messagebox.showinfo(" ","Deleted Successfully")

def update():
    query = ("UPDATE college_stu_sys SET student_name=%s,father_name=%s, gender=%s, Category=%s, branch=%s, year=%s, contact_no=%s, address=%s WHERE admission_no=%s",(nameentry.get(),father_nameentry.get(),genentry.get(),categentry.get(),yearentry.get(),contentry.get(),addrentry.get(),admi_noentry.get()))
    cur.execute(query)
    conn.commit()
    tkinter.messagebox.showinfo(" ","Updated Successfully")

root.geometry("700x550")
root.title(" Piyush Kushwaha Project on ...COLLEGE's STUDENTS MANAGEMENT SYSTEM...")

frame1 = Frame(root, bg='light grey', bd=5, relief=RIDGE)
frame1.place(x=2, y=0, width=1560, height=80)

lb = Label(frame1, text="College's Students Management System", font=("poppins 22 bold"), bg = 'bisque2', padx = 400, pady = 15)
lb.grid()


f = Frame(root, borderwidth=5, relief=GROOVE, bg = 'bisque2')
f.place(x = 2, y = 90, width = 680, height = 545)
l1 = Label(f,text="Admission number:",font=("poppins 11 bold"))
l2 = Label(f,text="Student Name:",font=("poppins 11 bold"))
l3 = Label(f,text="Father's name:",font=("poppins 11 bold"))
l4 = Label(f,text="Gender:",font=("poppins 11 bold"))
l5 = Label(f,text="Category:",font=("poppins 11 bold"))
l6 = Label(f,text="Branch:",font=("poppins 11 bold"))
l7 = Label(f,text="Year:",font=("poppins 11 bold"))
l8 = Label(f,text="Contact no.:",font=("poppins 11 bold"))
l9 = Label(f,text="Address:",font=("poppins 11 bold"))

photo = Image.open("1_photo.png")
resize_image = photo.resize((560,535))
ph = ImageTk.PhotoImage(resize_image)
lbl = Label(root,image = ph, bd = 5 ,relief = GROOVE, padx = 20, pady = 20 , bg = 'bisque2')
lbl.place(x=700, y = 90)


l1.grid(row=30, column=0, padx=10, pady=10,sticky=W)
l2.grid(row=31, column=0, padx=10, pady=10,sticky=W)
l3.grid(row=32, column=0, padx=10, pady=10,sticky=W)
l4.grid(row=33, column=0, padx=10, pady=10,sticky=W)
l5.grid(row=34, column=0, padx=10, pady=10,sticky=W)
l6.grid(row=35, column=0, padx=10, pady=10,sticky=W)
l7.grid(row=36, column=0, padx=10, pady=10,sticky=W)
l8.grid(row=37, column=0, padx=10, pady=10,sticky=W)
l9.grid(row=38, column=0, padx=10, pady=10,sticky=W)


admi_no = StringVar()
name = StringVar()
father_name = StringVar()
gen = StringVar()
categ =StringVar()
branch =StringVar()
year = StringVar()
cont = StringVar()
addr = StringVar()

admi_noentry = Entry(f, width=50, textvariable = admi_no)
nameentry = Entry(f, width=50, textvariable= name)
father_nameentry = Entry(f, width=50, textvariable= father_name)
genentry = ttk.Combobox (f, width=47, textvariable=gen)
categentry = ttk.Combobox(f, width=47, textvariable=categ)
branchentry = ttk.Combobox(f, width=47, textvariable=branch)
yearentry = ttk.Combobox(f, width=47, textvariable=year)
contentry = Entry(f, width=50, textvariable=cont)
addrentry = Entry(f, width=50, textvariable=addr)

genentry['values'] =('Female','Male','Other')
categentry['values'] =('SC/ST','OBC','Genral')
branchentry['values'] =('BCA','BBA','B.SC','B.A','B.com','B.tech')
yearentry['values'] =('Year 1','Year 2','Year 3','Year 4','Back Yr')


admi_noentry.grid(row=30, column=1, padx=100)
nameentry.grid(row=31, column=1, padx=100)
father_nameentry.grid(row=32, column=1, padx=100)
genentry.grid(row=33, column=1, padx=100)
categentry.grid(row=34, column=1, padx=100)
branchentry.grid(row=35, column=1, padx=100)
yearentry.grid(row=36, column=1, padx=100)
contentry.grid(row=37, column=1, padx=100)
addrentry.grid(row=38, column=1, padx=100)


b1 = Button(f, fg='red',text="Add",command=insert, padx=20, pady=10, font=("poppins 12 bold"))
b2 = Button(f, fg='red',text="Reset",command=reset, padx=20, pady=10, font=("poppins 12 bold"))
b3 = Button(f, fg='red',text="Delete",command=delete, padx=20, pady=10, font=("poppins 12 bold"))
b4 = Button(f, fg='red',text="Update",command=update, padx=20, pady=10, font=("poppins 12 bold"))
b1.place(x=260, y=420, width=80, height=45)
b2.place(x=260, y=480, width=80, height=45)
b3.place(x=490, y=420, width=80, height=45)
b4.place(x=490, y=480, width=80, height=45)

root.mainloop()















