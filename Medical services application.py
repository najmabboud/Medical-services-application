from tkinter import *
from tkinter import ttk
import webbrowser
import tkinter as tk
from email.mime.text import MIMEText
import smtplib
from tkcalendar import DateEntry
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import pymysql
from pyarabic.araby import strip_tashkeel
import textwrap
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("1000x700+100+50")


bkg = "#636e72"





def backk():
    fback=Frame(root,width=700,height=600)
    fback.place(x=0,y=50)





def sqldoctor():
    f_sqldoctor = Frame(root,width=700,height=550,bg=bkg)
    f_sqldoctor.place(x=0,y=50)




    def f1():
        l_sqldoctor = Label(f_sqldoctor, text="الاسم الكامل ", bg="white", fg="black",font=("Arial",15))
        l_sqldoctor.place(x=600, y=80)
        e_sqldoctor = Entry(f_sqldoctor, width=50)
        e_sqldoctor.place(x=130, y=80)
        l2_sqldoctor = Label(f_sqldoctor, text="الاختصاص  ", bg="white", fg="black",font=("Arial",15))
        l2_sqldoctor.place(x=600, y=130)
        
        def a1():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            z=e_sqldoctor.get()
    
            date_list1["values"] = []

            cur.execute("SELECT DISTINCT work FROM doctors WHERE fullname=%s  ORDER BY work ASC", (z,))
            dates = cur.fetchall()
            date_list1["values"] = [date[0] for date in dates]
            cur.close()
            b1.config(bg="red")

        date_list1 = ttk.Combobox(f_sqldoctor, values=[], state="readonly", width=40)
    
        date_list1.place(x=130, y=130)
        b1=Button(f_sqldoctor,text="✔",command=a1)
        b1.place(x=10,y=80)

        l3_sqldoctor = Label(f_sqldoctor, text="الايميل  ", bg="white", fg="black",font=("Arial",15))
        l3_sqldoctor.place(x=600, y=180)
        
        
        def a2():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            z=e_sqldoctor.get()
            d=date_list1.get()
    
            date_list2["values"] = []

            cur.execute("SELECT DISTINCT email FROM doctors WHERE fullname=%s AND work=%s  ORDER BY email ASC", (z,d))
            dates = cur.fetchall()
            date_list2["values"] = [date[0] for date in dates]
            cur.close()
            b2.config(bg="red")

        date_list2 = ttk.Combobox(f_sqldoctor, values=[], state="readonly", width=40,)
    
        date_list2.place(x=130, y=180)
        b2=Button(f_sqldoctor,text="✔",command=a2)
        b2.place(x=10,y=130)

        l4_sqldoctor = Label(f_sqldoctor, text="كلمة المرور  ", bg="white", fg="black",font=("Arial",15))
        l4_sqldoctor.place(x=600, y=220)

        def a3():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            z=date_list2.get()
            
    
            date_list3["values"] = []

            cur.execute("SELECT DISTINCT password FROM users WHERE email=%s  ORDER BY password ASC", (z,))
            dates = cur.fetchall()
            date_list3["values"] = [date[0] for date in dates]
            cur.close()
            b3.config(bg="red")

        date_list3 = ttk.Combobox(f_sqldoctor, values=[], state="readonly", width=40)
    
        date_list3.place(x=130, y=220)
        b3=Button(f_sqldoctor,text="✔",command=a3)
        b3.place(x=10,y=180)


        l5_sqldoctor = Label(f_sqldoctor, text=" التاريخ  ", bg="white", fg="black",font=("Arial",15))
        l5_sqldoctor.place(x=600, y=280)

        def a4():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            d=date_list2.get()
            
    
            date_list4["values"] = []

            cur.execute("SELECT DISTINCT date FROM dectorstimes WHERE dectoremail=%s  ORDER BY date ASC", (d,))
            dates = cur.fetchall()
            date_list4["values"] = [date[0] for date in dates]
            cur.close()
            b4.config(bg="red")

        date_list4 = ttk.Combobox(f_sqldoctor, values=[], state="readonly", width=40)
    
        date_list4.place(x=130, y=280)
        b4=Button(f_sqldoctor,text="✔",command=a4)
        b4.place(x=10,y=220)





        l6_sqldoctor = Label(f_sqldoctor, text=" الوقت  ", bg="white", fg="black",font=("Arial",15))
        l6_sqldoctor.place(x=600, y=310)



        def a5():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            d=date_list2.get()
            s=date_list4.get()
            
            
    
            date_list5["values"] = []

            cur.execute("SELECT DISTINCT time FROM dectorstimes WHERE dectoremail=%s And date=%s ORDER BY date ASC", (d,s,))
            dates = cur.fetchall()
            date_list5["values"] = [date[0] for date in dates]
            cur.close()
            b5.config(bg="red")

        date_list5 = ttk.Combobox(f_sqldoctor, values=[], state="readonly", width=40)
    
        date_list5.place(x=130, y=310)
        b5=Button(f_sqldoctor,text="✔",command=a5)
        b5.place(x=10,y=280)


        def sendok():
            eem = str(date_list2.get())
            hl = date_list5.get()
            dl = date_list4.get()

            if (eem== ""):
                MessageBox.showinfo("field")
            else:
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

                    #con = mysql.connect(host="localhost", user="root", password="", database='database')
                cur = con.cursor()
                cur.execute('SELECT customeremail  FROM dectorstimes WHERE dectoremail=%s AND date=%s AND time=%s',(eem,dl,hl) )

                res=cur.fetchall()
                con.commit()
                def rre():
                    for i in res :
                        return str(i[0])

                server = smtplib.SMTP_SSL("smtp.gmail.com", smtplib.SMTP_SSL_PORT)
                server.login(eem,date_list3.get())
                subject = "message"
                body = "تمت الموافقة على موعدك"
                mse = MIMEText(body)
                mse['To'] =rre()
                mse["From"] = eem
                mse["Subject"] = subject
                server.send_message(mse)

                MessageBox.showinfo("تم الارسال")
                con =  mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                    #con = mysql.connect(host="localhost", user="root", password="", database='database')
                cur = con.cursor()
                cur.execute('DELETE FROM `dectorstimes` WHERE date=%s AND time=%s', (date_list4.get(),date_list5.get()))
                con.commit()
                con.close()





        def sendno():
            eem = str(date_list2.get())
            hl = date_list5.get()
            dl = date_list4.get()

            if (eem== ""):
                MessageBox.showinfo("field")
            else:
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

                    #con = mysql.connect(host="localhost", user="root", password="", database='database')
                cur = con.cursor()
                cur.execute('SELECT customeremail  FROM dectorstimes WHERE dectoremail=%s AND date=%s AND time=%s',(eem,dl,hl) )

                res=cur.fetchall()
                con.commit()
                def rre():
                    for i in res :
                        return str(i[0])

                server = smtplib.SMTP_SSL("smtp.gmail.com", smtplib.SMTP_SSL_PORT)
                server.login(eem,date_list3.get())
                subject = "message"
                body = "  لم تتم الموافقة على موعدك  "
                mse = MIMEText(body)
                mse['To'] =rre()
                mse["From"] = eem
                mse["Subject"] = subject
                server.send_message(mse)

                MessageBox.showinfo("تم الارسال")
                con =  mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                    #con = mysql.connect(host="localhost", user="root", password="", database='database')
                cur = con.cursor()
                cur.execute('DELETE FROM `dectorstimes` WHERE date=%s AND time=%s', (date_list4.get(),date_list5.get()))
                con.commit()
                con.close()






        b_ok = Button(f_sqldoctor,text="موافقة",bg="black",fg="white",width=30,command=sendok,font=("Arial",15))
        b_ok.place(x=400,y=400)
        b_no = Button(f_sqldoctor,text="رفض",bg="black",fg="white",width=30,command=sendno,font=("Arial",15))
        b_no.place(x=50,y=400)








    b1_sqldoctor = Button(f_sqldoctor,text="الاستعلام عن مواعيدي",width=50,bg="black",fg="white",cursor="hand2",command=f1,font=("Arial",15))
    b1_sqldoctor.place(x=10,y=30)





def pas():
    
    fpas = Frame(root,width=700,height=550,)
    fpas.place(x=0,y=50)
    
    l1 =Label(fpas,text="الايميل   ",bg="black",fg="white",font=("Arial",15))
    l1.place(x=550,y=100)
        
    e1=Entry(fpas,width=60)
    e1.place(x=130,y=100)
    
    l2 =Label(fpas,text="كلمة المرور   ",bg="black",fg="white",font=("Arial",15))
    l2.place(x=550,y=200)
        
    e2=Entry(fpas,width=60)
    e2.place(x=130,y=200)
    
    
    
    def auth():
        e11=e1.get()
        e22=e2.get()
        
        con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')       
        #con = mysql.connect(host="localhost", user="root", password="", database='database')
        cur = con.cursor()
        
        cur.execute("SELECT DISTINCT passwordt FROM users WHERE email=%s   ORDER BY email ASC", (e11,))
        out = (cur.fetchone()[0])
        
        
        if (e22==out):
            sqldoctor()
        else:
            MessageBox.showinfo("ok","كلمة المرور خطأ")
            
        
        
    
    
    
    
    
    
    b1 = Button(fpas,text="التالي ",width=40,bg="black",fg="white",font=("Arial",15),command=auth)
    b1.place(x=100,y=400)
    






def mainn():

    
    fmain = Frame(root,width=700,height=550,)
    fmain.place(x=0,y=50)
    
    image2 = Image.open("C:\\Users\\ASUS\\Desktop\\6.jpeg")
    image2=image2.resize((700,550))
    test = ImageTk.PhotoImage(image2)

    label1 = Label(fmain,image=test)
    label1.image = test

    label1.place(x=0,y=0)
    

    

    
    

    

    def page3_2():
        #con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

        con = mysql.connect(host="localhost", user="root", password="", database='database')
        cur = con.cursor()
        
        f_page3_2 = Frame(root,width=700,height=550,bg=bkg)
        f_page3_2.place(x=0,y=50)

        l_page3_2 = Label(f_page3_2,text="ادخل المعلومات التالية",bg="black",fg="white",font=("Arial",15))
        l_page3_2.place(x=100,y=10)
        
        

        

        l1_page3_2 =Label(f_page3_2,text="اسم الطبيب ",bg="black",fg="white",font=("Arial",15))
        l1_page3_2.place(x=600,y=50)

        l2_page3_2 =Label(f_page3_2,text=" اختصاصه",bg="black",fg="white",font=("Arial",15))
        l2_page3_2.place(x=600,y=90)


        l3_page3_2 =Label(f_page3_2,text="ايميل الطبيب ",bg="black",fg="white",font=("Arial",15))
        l3_page3_2.place(x=600,y=130)
        
        ll3_page3_2 =Label(f_page3_2,text="ايميلك  ",bg="black",fg="white",font=("Arial",15))
        ll3_page3_2.place(x=600,y=170)
        

        
        
        lll3_page3_2 =Label(f_page3_2,text="كلمة المرور  ",bg="black",fg="white",font=("Arial",15))
        lll3_page3_2.place(x=600,y=210)
        
        e1=Entry(f_page3_2,width=60)
        e1.place(x=130,y=50)

        def a1():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            z=e1.get()
    
            date_list1["values"] = []

            cur.execute("SELECT DISTINCT work FROM doctors WHERE fullname=%s   ORDER BY work ASC", (z,))
            dates = cur.fetchall()
            date_list1["values"] = [date[0] for date in dates]
            cur.close()
            b1.config(bg="red")


        date_list1 = ttk.Combobox(f_page3_2, values=[], state="readonly", width=40)
        date_list1.place(x=130, y=90)
        b1=Button(f_page3_2,text="✔",command=a1)
        b1.place(x=10,y=50)
        
        

        def a2():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            z=e1.get()
            x1=date_list1.get()
            date_list2["values"] = []

            cur.execute("SELECT DISTINCT email FROM doctors WHERE fullname=%s AND work=%s  ORDER BY work ASC", (z,x1))
            dates = cur.fetchall()
            date_list2["values"] = [date[0] for date in dates]
            cur.close()
            b2.config(bg="red")


        date_list2 = ttk.Combobox(f_page3_2, values=[], state="readonly", width=40)
        date_list2.place(x=130, y=130)
        b2=Button(f_page3_2,text="✔",command=a2)
        b2.place(x=10,y=90)

        e2=Entry(f_page3_2,width=60)
        e2.place(x=130,y=170)
        def a3():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            d=e2.get()
            date_list3["values"] = []

            cur.execute("SELECT DISTINCT password FROM users WHERE email=%s  ORDER BY password ASC", (d,))
            dates = cur.fetchall()
            date_list3["values"] = [date[0] for date in dates]
            cur.close()
            b3.config(bg="red")


        date_list3 = ttk.Combobox(f_page3_2, values=[], state="readonly", width=40)
        date_list3.place(x=130, y=210)
        b3=Button(f_page3_2,text="✔",command=a3)
        b3.place(x=10,y=170)









        l4_page3_2 =Label(f_page3_2,text="الموعد",bg="black",fg="white",font=("Arial",15))
        l4_page3_2.place(x=600,y=250)
        l5_page3_2 =Label(f_page3_2,text="التاريخ",bg="black",fg="white",font=("Arial",15))
        l5_page3_2.place(x=600,y=300)
        e5_page3_2 =DateEntry(f_page3_2,width=25,date_pattern="d/m/y",font=("Arial",20))
        e5_page3_2.place(x=5,y=300)
        l6_page3_2 =Label(f_page3_2,text="الوقت",bg="black",fg="white",font=("Arial",15))
        l6_page3_2.place(x=600,y=350)
        options =["8:00 am", "8:30 am", "9:00 am","9:30 am"]
        e6_page3_2 =ttk.Combobox(f_page3_2, values=options,font=("Arial",15))
        e6_page3_2.place(x=5,y=350)



        def sendd():
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='database')
            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            cur.execute('SELECT COUNT(*) FROM dectorstimes WHERE date = %s AND time=%s', (e5_page3_2.get(),e6_page3_2.get()))
            result =cur.fetchone()[0]
            if result > 0:

                MessageBox.showinfo("الموعد محجوز سابقا")
            else:
                query ='INSERT INTO `dectorstimes` (`dectoremail`, `customeremail`, `date`, `time`) VALUES(%s,%s,%s,%s)'
                val = (date_list2.get(),e2.get(), e5_page3_2.get(), e6_page3_2.get())
                cur.execute(query, val)
                MessageBox.showinfo("تمت اضافة موعدك")
                con.commit()
                con.close()
                server = smtplib.SMTP_SSL("smtp.gmail.com",smtplib.SMTP_SSL_PORT)
                server.login(e2.get(),date_list3.get())
                subject = "لديك حجز جديد"
                body = "date   "+e5_page3_2.get()+"\n "+"time   "+e6_page3_2.get()
                mse = MIMEText(body)
                mse['To'] = date_list2.get()
                mse["From"] = e2.get()
                mse["Subject"] = subject
                server.send_message(mse)
                #page4()





        b_page3_2 = Button(f_page3_2,text="التالي",width=40,bg="black",fg="white",command=sendd,font=("Arial",15))
        b_page3_2.place(x=0,y=500)

        
        


    
    def page3_3():
        f_page3_3 = Frame(root,width=700,height=550,bg=bkg)
        f_page3_3.place(x=0,y=50)

        l_page3_3 = Label(f_page3_3,text="ادخل المعلومات التالية",bg="black",fg="white",font=("Arial",15))
        l_page3_3.place(x=100,y=10)

        l1_page3_3 =Label(f_page3_3,text=" الاسم",bg="black",fg="white",font=("Arial",15))
        l1_page3_3.place(x=600,y=50)
        e1_page3_3 = Entry(f_page3_3,width=40)
        e1_page3_3.place(x=130,y=50)


        l2_page3_3 =Label(f_page3_3,text="الايميل ",bg="black",fg="white",font=("Arial",15))
        l2_page3_3.place(x=600,y=100)

        def a1():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            z=e1_page3_3.get()
    
            date_list1["values"] = []

            cur.execute("SELECT DISTINCT email FROM users WHERE fullname=%s  ORDER BY email ASC", (z,))
            dates = cur.fetchall()
            date_list1["values"] = [date[0] for date in dates]
            cur.close()
            b1.config(bg="red")

        date_list1 = ttk.Combobox(f_page3_3, values=[], state="readonly", width=40)
    
        date_list1.place(x=130, y=100)
        b1=Button(f_page3_3,text="✔",command=a1)
        b1.place(x=10,y=50)



        l3_page3_3 =Label(f_page3_3,text="كلمة المرور",bg="black",fg="white",font=("Arial",15))
        l3_page3_3.place(x=600,y=150)

        def a2():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            z=e1_page3_3.get()
            d=date_list1.get()
    
            date_list2["values"] = []

            cur.execute("SELECT DISTINCT password FROM users WHERE fullname=%s AND email=%s  ORDER BY email ASC", (z,d,))
            dates = cur.fetchall()
            date_list2["values"] = [date[0] for date in dates]
            cur.close()
            b2.config(bg="red")

        date_list2 = ttk.Combobox(f_page3_3, values=[], state="readonly", width=40)
    
        date_list2.place(x=130, y=150)
        b2=Button(f_page3_3,text="✔",command=a2)
        b2.place(x=10,y=100)
        
        

        ll3_page3_3 =Label(f_page3_3,text="اسم الطبيب",bg="black",fg="white",font=("Arial",15))
        ll3_page3_3.place(x=600,y=200)
        
        e2 = Entry(f_page3_3,width=40)
        e2.place(x=130,y=200)
        
        ll33_page3_3 =Label(f_page3_3,text="الاختصاص",bg="black",fg="white",font=("Arial",15))
        ll33_page3_3.place(x=600,y=250)
        
        
        
        def a3():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            z=e2.get()
            
    
            date_list3["values"] = []

            cur.execute("SELECT DISTINCT work FROM doctors WHERE fullname=%s   ORDER BY work ASC", (z,))
            dates = cur.fetchall()
            date_list3["values"] = [date[0] for date in dates]
            cur.close()
            b3.config(bg="red")

        date_list3 = ttk.Combobox(f_page3_3, values=[], state="readonly", width=40)
    
        date_list3.place(x=130, y=250)
        b3=Button(f_page3_3,text="✔",command=a3)
        b3.place(x=10,y=200)

        lll3_page3_3 =Label(f_page3_3,text="ايميل الطبيب ",bg="black",fg="white",font=("Arial",15))
        lll3_page3_3.place(x=600,y=300)

        def a4():
            con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="localhost", user="root", password="", database='database')
            cur = con.cursor()
            z=e2.get()
            d=date_list3.get()
    
            date_list4["values"] = []

            cur.execute("SELECT DISTINCT email FROM doctors WHERE fullname=%s AND work=%s   ORDER BY work ASC", (z,d,))
            dates = cur.fetchall()
            date_list4["values"] = [date[0] for date in dates]
            cur.close()
            b4.config(bg="red")

        date_list4 = ttk.Combobox(f_page3_3, values=[], state="readonly", width=40)
    
        date_list4.place(x=130, y=300)
        b4=Button(f_page3_3,text="✔",command=a4)
        b4.place(x=10,y=250)



        l4_page3_3 =Label(f_page3_3,text="الاستشارة",bg="black",fg="white",font=("Arial",15))
        l4_page3_3.place(x=600,y=350)

        e4_page3_3 = Entry(f_page3_3,width=70)
        e4_page3_3.place(x=5,y=350)


        def sendd():
            server = smtplib.SMTP_SSL("smtp.gmail.com",smtplib.SMTP_SSL_PORT)
            server.login(date_list1.get(),date_list2.get())
            subject = "message"
            body = e4_page3_3.get()
            mse = MIMEText(body)
            mse['To'] = date_list4.get()
            mse["From"] = date_list1.get()
            mse["Subject"] = subject
            server.send_message(mse)
            #page4()





        b_page4 = Button(f_page3_3,text="ارسال ",width=40,bg="black",fg="white",command=sendd,font=("Arial",15))
        b_page4.place(x=0,y=400)



    
    b1main = Button(fmain,width=50,height=2,text="احجز موعدك",bg="white",fg="black",command=page3_2,font=("Arial",15))
    b1main.place(x=50,y=100)
    b2main = Button(fmain,width=50,height=2,text=" استشر طبيبك",bg="white",fg="black",font=("Arial",15),command=page3_3)
    b2main.place(x=50,y=200)
    b3main = Button(fmain,width=50,height=2,text=" استعلم عن مواعيدك",bg="white",fg="black",font=("Arial",15),command=pas)
    b3main.place(x=50,y=300)
    
    






def updatetime():
    f_updatetime = Frame(root,width=700,height=550,bg=bkg)
    f_updatetime.place(x=0,y=50)
    l_updatetime = Label(f_updatetime,text="ادخل معلومات الحجز",bg="black",fg="white",font=("Arial",15))
    l_updatetime.place(x=100,y=10)

    l1_updatetime =Label(f_updatetime,text="الاسم ",bg="black",fg="white",font=("Arial",15))
    l1_updatetime.place(x=600,y=50)
    e1_updatetime= Entry(f_updatetime,width=30)
    e1_updatetime.place(x=130,y=50)



    l1_updatetime =Label(f_updatetime,text="ايميلك الخاص",bg="black",fg="white",font=("Arial",15))
    l1_updatetime.place(x=600,y=100)

    def a1():
        con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        #con = mysql.connect(host="localhost", user="root", password="", database='database')
        cur = con.cursor()
        z=e1_updatetime.get()
    
        date_list1["values"] = []

        cur.execute("SELECT DISTINCT email FROM users WHERE fullname=%s  ORDER BY email ASC", (z,))
        dates = cur.fetchall()
        date_list1["values"] = [date[0] for date in dates]
        cur.close()
        b1.config(bg="red")

    date_list1 = ttk.Combobox(f_updatetime, values=[], state="readonly", width=40)
    
    date_list1.place(x=130, y=100)
    b1=Button(f_updatetime,text="✔",command=a1)
    b1.place(x=10,y=50)


    l2_updatetime =Label(f_updatetime,text=" كلمة المرور",bg="black",fg="white",font=("Arial",15))
    l2_updatetime.place(x=600,y=150)


    def a2():
        con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        #con = mysql.connect(host="localhost", user="root", password="", database='database')
        cur = con.cursor()
        z=date_list1.get()
    
        date_list2["values"] = []

        cur.execute("SELECT DISTINCT password FROM users WHERE email=%s  ORDER BY password ASC", (z,))
        dates = cur.fetchall()
        date_list2["values"] = [date[0] for date in dates]
        cur.close()
        b2.config(bg="red")

    date_list2 = ttk.Combobox(f_updatetime, values=[], state="readonly", width=40)
    
    date_list2.place(x=130, y=150)
    b2=Button(f_updatetime,text="✔",command=a2)
    b2.place(x=10,y=100)







    l3_updatetime =Label(f_updatetime,text="اسم الطبيب ",bg="black",fg="white",font=("Arial",15))
    l3_updatetime.place(x=600,y=200)
    e3_updatetime = Entry(f_updatetime,width=30)
    e3_updatetime.place(x=130,y=200)
    
    ll3_updatetime =Label(f_updatetime,text="اختصاصه  ",bg="black",fg="white",font=("Arial",15))
    ll3_updatetime.place(x=600,y=250)
    
    
    
    def a3():
        con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        #con = mysql.connect(host="localhost", user="root", password="", database='database')
        cur = con.cursor()
        z=e3_updatetime.get()
    
        date_list3["values"] = []

        cur.execute("SELECT DISTINCT work FROM doctors WHERE fullname=%s  ORDER BY work ASC", (z,))
        dates = cur.fetchall()
        date_list3["values"] = [date[0] for date in dates]
        cur.close()
        b3.config(bg="red")

    date_list3 = ttk.Combobox(f_updatetime, values=[], state="readonly", width=40)
    
    date_list3.place(x=130, y=250)
    b3=Button(f_updatetime,text="✔",command=a3)
    b3.place(x=10,y=200)

    
    
    

    l4_updatetime =Label(f_updatetime,text="ايميل الطبيب  ",bg="black",fg="white",font=("Arial",15))
    l4_updatetime.place(x=600,y=300)
    
    
    def a4():
        con=mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        #con = mysql.connect(host="localhost", user="root", password="", database='database')
        cur = con.cursor()
        z=e3_updatetime.get()
        d=date_list3.get()
    
        date_list4["values"] = []

        cur.execute("SELECT DISTINCT email FROM doctors WHERE fullname=%s AND work=%s ORDER BY email ASC", (z,d,))
        dates = cur.fetchall()
        date_list4["values"] = [date[0] for date in dates]
        cur.close()
        b4.config(bg="red")

    date_list4 = ttk.Combobox(f_updatetime, values=[], state="readonly", width=40)
    
    date_list4.place(x=130, y=300)
    b4=Button(f_updatetime,text="✔",command=a4)
    b4.place(x=10,y=250)



    l5_updatetime =Label(f_updatetime,text="التاريخ",bg="black",fg="white",font=("Arial",15))
    l5_updatetime.place(x=600,y=350)
    e5_updatetime =DateEntry(f_updatetime,width=25,date_pattern="d/m/y")
    e5_updatetime.place(x=5,y=350)
    l6_updatetime =Label(f_updatetime,text="الوقت",bg="black",fg="white",font=("Arial",15))
    l6_updatetime.place(x=600,y=400)
    options =["8:00 am", "8:30 am", "9:00 am","9:30 am"]
    e6_updatetime =ttk.Combobox(f_updatetime, values=options)
    e6_updatetime.place(x=5,y=400)

    def deletetime():
        eup1 = date_list1.get()
        eup2 = date_list4.get()
        eup3 = e5_updatetime.get()
        eup4 = e6_updatetime.get()
        epass = date_list2.get()
        if (eup1 =="" or eup2=="" or eup3=="" or eup4 ==""):
            MessageBox.showinfo("field")
        else:
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='sql12623107')
            #con = mysql.connect(host="localhost",user="root",password="",database='database')
            cur = con.cursor()
            cur.execute('DELETE FROM `dectorstimes` WHERE customeremail=%s AND dectoremail=%s AND date=%s AND time=%s',(eup1,eup2,eup3,eup4))
            MessageBox.showinfo("sucsess delete")
            con.commit()
            con.close()
            server = smtplib.SMTP_SSL("smtp.gmail.com",smtplib.SMTP_SSL_PORT)
            server.login(eup1,epass)
            subject = "تم الغاء الموعد التالي"
            body = "date   "+eup3+"\n "+"time   "+eup4
            mse = MIMEText(body)
            mse['To'] = eup2
            mse["From"] = eup1
            mse["Subject"] = subject
            server.send_message(mse)


    def refresh():
        v1 = date_list1.get()
        v2 = date_list4.get()
        if (v1 =="" or v2=="" ):
            MessageBox.showinfo("field")
        else:
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='sql12623107')
            #con = mysql.connect(host="localhost",user="root",password="",database='database')
            cur = con.cursor()
            cur.execute('SELECT `date`, `time` FROM `dectorstimes` WHERE customeremail=%s AND dectoremail=%s',(v1,v2))
            #MessageBox.showinfo("sucsess")
            rr = str(cur.fetchall()[0])
            
            con.commit()
            con.close()

        f_refresh = Frame(root,width=700,height=550,bg=bkg)
        f_refresh.place(x=0,y=50)

        l1_refresh = Label(f_refresh,text="التاريخ الجديد",bg="black",fg="white",font=("Arial",15))
        l1_refresh.place(x=600,y=50)

        e1_refresh= DateEntry(f_refresh, width=25, date_pattern="d/m/y",font=("Arial",15))
        e1_refresh.place(x=50, y=50)

        l2_refresh = Label(f_refresh, text="الوقت", bg="black", fg="white",font=("Arial",15))
        l2_refresh.place(x=600, y=100)
        options = ["8:00 am", "8:30 am", "9:00 am", "9:30 am"]
        e2_refresh= ttk.Combobox(f_refresh, values=options,width=40)
        e2_refresh.place(x=50, y=100)

        def up():
            z1=date_list1.get()
            z2=date_list4.get()
            z3=date_list2.get()
            z4=e1_refresh.get()
            z5=e2_refresh.get()

            if (z1 == "" or z2 == ""  or z4 == "" or z5==""):
                MessageBox.showinfo("field")
            else:
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                #con = mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='sql12623107')
                #con = mysql.connect(host="localhost", user="root", password="", database='database')
                cur = con.cursor()
                cur.execute(
                    'UPDATE `dectorstimes` SET `date`=%s,`time`=%s  WHERE  customeremail=%s AND dectoremail=%s',(z4,z5,z1,z2))

                MessageBox.showinfo("sucsess up")
                con.commit()
                con.close()

                server = smtplib.SMTP_SSL("smtp.gmail.com", smtplib.SMTP_SSL_PORT)
                server.login(z1,z3)
                subject = "تم تغيير الموعد التالي "
                body = "date   " + rr + "\n " + "الى   " + "\n"+"date"+z4+"\n"+"time"+z5
                mse = MIMEText(body)
                mse['To'] = z2
                mse["From"] = z1
                mse["Subject"] = subject
                server.send_message(mse)





        b1_refresh = Button(f_refresh,text="تحديث",width=40,bg="black",fg="white",cursor="hand2",command=up,font=("Arial",20))
        b1_refresh.place(x=5,y=200)

        b2_refresh = Button(f_refresh,text="عودة",width=40,bg="black",fg="white",command=updatetime,font=("Arial",20))
        b2_refresh.place(x=5,y=250)






    b1_updatetime = Button(f_updatetime,text="حذف موعيدي",bg="black",fg="white",width=40,cursor="hand2",command=deletetime,font=("Arial",15))
    b1_updatetime.place(x=5,y=450)

    b2_updatetime = Button(f_updatetime,text="تعديل الموعد",bg="black",fg="white",width=40,cursor="hand2",command=refresh,font=("Arial",15))
    b2_updatetime.place(x=5,y=500)


def get_info_doctor():
    f_get_info_doctor = Frame(root,width=700,height=550,bg=bkg)
    f_get_info_doctor.place(x=0,y=50)

    l1_get_info_doctor = Label(f_get_info_doctor,text="ادخل اسم الطبيب الكامل",bg="white",fg="black",font=("Arial",15))
    l1_get_info_doctor.place(x=510,y=50)

    e1_get_info_doctor = Entry(f_get_info_doctor,width=70)
    e1_get_info_doctor.place(x=5,y=50)


    def ddd():
        def populate_dates2():
            z = e1_get_info_doctor.get()
            connection = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #connection = mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='sql12623107')
            #connection = pymysql.connect(host="localhost", user="root", password="", db="database")
            cursor = connection.cursor()
            # clear the options of the first dropdown list
            date_list2["values"] = []

            # query the database for dates
            cursor.execute("SELECT DISTINCT work FROM doctors WHERE fullname=%s  ORDER BY work ASC", (z,))
            dates = cursor.fetchall()

            # populate the first dropdown list with the dates
            date_list2["values"] = [date[0] for date in dates]
            connection.close()

        date_list2 = ttk.Combobox(f_get_info_doctor, values=[], state="readonly", width=40)
        populate_dates2()
        date_list2.place(x=5, y=110)

        def ss():

            l3_get_info_doctor = Label(f_get_info_doctor,text="مالذي تريد الحصول علية؟",bg="white",fg="black",font=("Arial",15))
            l3_get_info_doctor.place(x=510,y=150)

            combogender_get_info_doctor = ttk.Combobox(f_get_info_doctor, state='readonly', width=10, font=('Calibri', 15))
            combogender_get_info_doctor['values'] = ("الايميل", "ايام المشفى","ايام العيادة","ساعات الدوام")
            combogender_get_info_doctor.place(x=100, y=200)

            def result_info_doctors():
                ee1 = e1_get_info_doctor.get()
                ee2 = date_list2.get()
                ee3 = combogender_get_info_doctor.get()
                conn = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                #conn = mysql.connect(host="localhost", user="root", password="", database='database')
                cursor = conn.cursor()
                if (ee1 == "" or ee2 == "" or ee3 == ""):
                    MessageBox.showinfo("field")
                elif (ee3 == "الايميل"):
                    cursor.execute("SELECT email FROM doctors WHERE fullname=%s AND work=%s ", (ee1, ee2))
                    result = cursor.fetchone()

                    l1 = Text(f_get_info_doctor, width=70, height=10, wrap="word")
                    l1.insert("1.0", result)
                    l1.place(x=5, y=310)
                    conn.close()
                elif (ee3 == "ايام المشفى"):
                    cursor.execute("SELECT dayinhospital FROM doctors WHERE fullname=%s AND work=%s ", (ee1, ee2))
                    result = cursor.fetchone()
                    l1 = Text(f_get_info_doctor, width=70, height=10, wrap="word")
                    l1.insert("1.0", str(result))
                    l1.place(x=5, y=310)
                    conn.close()

                elif (ee3 == "ايام العيادة"):
                    cursor.execute("SELECT dayinhome FROM doctors WHERE fullname=%s AND work=%s ", (ee1, ee2))
                    result = cursor.fetchone()
                    l1 = Text(f_get_info_doctor, width=70, height=10, wrap="word")
                    l1.insert("1.0", result)
                    l1.place(x=5, y=310)
                    conn.close()

                elif (ee3 == "ساعات الدوام"):
                    cursor.execute("SELECT hourofwork FROM doctors WHERE fullname=%s AND work=%s ", (ee1, ee2))
                    result = cursor.fetchone()

                    l1 = Text(f_get_info_doctor, width=70, height=10,wrap="word")
                    l1.insert("0.0", result)
                    l1.place(x=10, y=310)




                    conn.close()

            b1_get_info_doctor = Button(f_get_info_doctor, text="التالي", width=40, bg="black", fg="white",
                                        cursor="hand2", command=result_info_doctors,font=("Arial",15))
            b1_get_info_doctor.place(x=5, y=250)




        bt=Button(f_get_info_doctor,text="التالي",width=10,bg="black",fg="white",command=ss,font=("Arial",15))
        bt.place(x=100,y=140)

    bb2_get_info_doctor = Button(f_get_info_doctor,text="الاختصاص",bg="white",fg="black",cursor="hand2",command=ddd,font=("Arial",15))
    bb2_get_info_doctor.place(x=100,y=80)








def customer():
    backk()
    fdoctor =Frame(root,width=190,height=550)
    fdoctor.place(x=800,y=50)
    
    image2 = Image.open("C:\\Users\\ASUS\\Desktop\\6.jpeg")
    image2=image2.resize((700,590))
    test = ImageTk.PhotoImage(image2)

    label1 = Label(root,image=test)
    label1.image = test

    label1.place(x=0,y=50)
    
    
    
    def hide():
        fdoctor =Frame(root,width=190,height=550)
        fdoctor.place(x=800,y=50)
        

        

    b11doctor = Button(fdoctor,height=2,text="❌",fg="black",font=("Arial",15),command=hide)
    b11doctor.place(x=100,y=0)
    
    b1doctor = Button(fdoctor,width=15,height=2,text="تعديل موعد/حذف ",fg="black",font=("Arial",15),command=updatetime)
    b1doctor.place(x=0,y=100)
    
    b2doctor = Button(fdoctor,width=15,height=2,text="معلومات الطبيب",fg="black",font=("Arial",15),command=get_info_doctor)
    b2doctor.place(x=0,y=300)
    



def login_doctors():
    f_login_doctors = Frame(root,width=700,height=550,bg=bkg)
    f_login_doctors.place(x=0,y=50)
    

    

    l1_login_doctors = Label(f_login_doctors,text="الاسم الكامل ",bg="black",fg="white",font=("Arial",15))
    l1_login_doctors.place(x=600,y=50)
    e1_login_doctors = Entry(f_login_doctors,width=50  )
    e1_login_doctors.place(x=5,y=50)

    l2_login_doctors = Label(f_login_doctors,text="الاختصاص ",bg="black",fg="white",font=("Arial",15))
    l2_login_doctors.place(x=600,y=100)
    e2_login_doctors = Entry(f_login_doctors,width=50)
    e2_login_doctors.place(x=5,y=100)

    l3_login_doctors = Label(f_login_doctors,text="الايميل ",bg="black",fg="white",font=("Arial",15))
    l3_login_doctors.place(x=600,y=150)
    e3_login_doctors = Entry(f_login_doctors,width=50)
    e3_login_doctors.place(x=5,y=150)

    l4_login_doctors = Label(f_login_doctors,text="ايام المشفى",bg="black",fg="white",font=("Arial",15))
    l4_login_doctors.place(x=600,y=200)
    
    l=Label(f_login_doctors,text="الأحد",fg="black",bg=bkg)
    l.place(x=10,y=180)
    
    tt1=ttk.Combobox(f_login_doctors,width=7)
    tt1['values']=("الاحد")
    
    tt1.place(x=5,y=200)
    
    l2=Label(f_login_doctors,text="الاثنين",fg="black",bg=bkg)
    l2.place(x=100,y=180)
    
    tt2=ttk.Combobox(f_login_doctors,values="الاثنين",width=7)
    
    tt2.place(x=90,y=200)
    
    l3=Label(f_login_doctors,text="الثلاثاء",fg="black",bg=bkg)
    l3.place(x=190,y=180)
    
    tt3=ttk.Combobox(f_login_doctors,values="الثلاثاء",width=7)
    
    tt3.place(x=180,y=200)
    
    l4=Label(f_login_doctors,text="الأربعاء",fg="black",bg=bkg)
    l4.place(x=280,y=180)
    
    tt4=ttk.Combobox(f_login_doctors,values="الاربعاء",width=7)
    
    tt4.place(x=270,y=200)
    
    l5=Label(f_login_doctors,text="الخميس",fg="black",bg=bkg)
    l5.place(x=370,y=180)
    
    tt5=ttk.Combobox(f_login_doctors,values="الخميس",width=7)
    
    tt5.place(x=360,y=200)
    
    l6=Label(f_login_doctors,text="الجمعه",fg="black",bg=bkg)
    l6.place(x=460,y=180)
    
    tt6=ttk.Combobox(f_login_doctors,values="الجمعه",width=7)
    
    tt6.place(x=450,y=200)
    
    l7=Label(f_login_doctors,text="السبت",fg="black",bg=bkg)
    l7.place(x=540,y=180)
    
    tt7=ttk.Combobox(f_login_doctors,values="السبت",width=7)
    
    tt7.place(x=530,y=200)

    

    l5_login_doctors = Label(f_login_doctors,text="ايام العيادة",bg="black",fg="white",font=("Arial",15))
    l5_login_doctors.place(x=600,y=300)

    
    ll=Label(f_login_doctors,text="الأحد",fg="black",bg=bkg)
    ll.place(x=10,y=280)
    
    ttt1=ttk.Combobox(f_login_doctors,values="الاحد",width=7)
    
    ttt1.place(x=5,y=300)
    
    ll2=Label(f_login_doctors,text="الاثنين",fg="black",bg=bkg)
    ll2.place(x=100,y=280)
    
    ttt2=ttk.Combobox(f_login_doctors,values="الاثنين",width=7)
    
    ttt2.place(x=90,y=300)
    
    ll3=Label(f_login_doctors,text="الثلاثاء",fg="black",bg=bkg)
    ll3.place(x=190,y=280)
    
    ttt3=ttk.Combobox(f_login_doctors,values="الثلاثاء",width=7)
    
    ttt3.place(x=180,y=300)
    
    ll4=Label(f_login_doctors,text="الأربعاء",fg="black",bg=bkg)
    ll4.place(x=280,y=280)
    
    ttt4=ttk.Combobox(f_login_doctors,values="الاربعاء",width=7)
    
    ttt4.place(x=270,y=300)
    
    ll5=Label(f_login_doctors,text="الخميس",fg="black",bg=bkg)
    ll5.place(x=370,y=280)
    
    ttt5=ttk.Combobox(f_login_doctors,values="الخميس",width=7)
    
    ttt5.place(x=360,y=300)
    
    ll6=Label(f_login_doctors,text="الجمعه",fg="black",bg=bkg)
    ll6.place(x=460,y=280)
    
    ttt6=ttk.Combobox(f_login_doctors,values="الجمعه",width=7)
    
    ttt6.place(x=450,y=300)
    
    ll7=Label(f_login_doctors,text="السبت",fg="black",bg=bkg)
    ll7.place(x=540,y=280)
    
    ttt7=ttk.Combobox(f_login_doctors,values="السبت",width=7)
    
    ttt7.place(x=530,y=300)
    
    

    l6_login_doctors = Label(f_login_doctors,text="ساعات الدوام ",bg="black",fg="white",font=("Arial",15))
    l6_login_doctors.place(x=600,y=390)

    e6_login_doctors=Entry(f_login_doctors,width=80)
    e6_login_doctors.place(x=5,y=390)    

    




    def add():
        e1 = e1_login_doctors.get()
        e2 = e2_login_doctors.get()
        e3 = e3_login_doctors.get()
        e4=str(tt1.get()+"-"+tt2.get()+"-"+tt3.get()+"-"+tt4.get()+"-"+tt5.get()+"-"+tt6.get()+"-"+tt7.get())
        e5=str(ttt1.get()+"-"+ttt2.get()+"-"+ttt3.get()+"-"+ttt4.get()+"-"+ttt5.get()+"-"+ttt6.get()+"-"+ttt7.get())
        e6 = e6_login_doctors.get()

        if (e1=="" or e2=="" or e3==""or e4==""or e5==""or e6=="" ):
            MessageBox.showinfo("الحقول مطلوبه")
        else:
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con=mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='sql12623107')
            #con = mysql.connect(host="localhost",user="root",password="",database='database')
            cur = con.cursor()
            query = 'INSERT INTO `doctors`(`fullname`, `work`, `email`, `dayinhospital`, `dayinhome`, `hourofwork`) VALUES(%s,%s,%s,%s,%s,%s)'
            val = (e1,e2,e3,e4,e5,e6)
            cur.execute(query, val)
            e1_login_doctors.delete(0,END)
            e2_login_doctors.delete(0,END)
            e3_login_doctors.delete(0, END)
            tt1.delete(0,END)
            tt2.delete(0,END)
            tt3.delete(0,END)
            tt4.delete(0,END)
            tt5.delete(0,END)
            tt6.delete(0,END)
            tt7.delete(0,END)
            ttt1.delete(0,END)
            ttt2.delete(0,END)
            ttt3.delete(0,END)
            ttt4.delete(0,END)
            ttt5.delete(0,END)
            ttt6.delete(0,END)
            ttt7.delete(0,END)
            e6_login_doctors.delete(0, END)

            MessageBox.showinfo("✔", "تمت العملية بنجاح")
            con.commit()
            con.close()


    b1_login_doctors = Button(f_login_doctors,text="ارسال",width=40,bg="black",fg="white",cursor="hand2",command=add)
    b1_login_doctors.place(x=5,y=500)




def pas3():
    
    ffpas = Frame(root,width=700,height=550,)
    ffpas.place(x=0,y=50)
    
    fl1 =Label(ffpas,text="الايميل   ",bg="black",fg="white",font=("Arial",15))
    fl1.place(x=550,y=100)
        
    fe1=Entry(ffpas,width=60)
    fe1.place(x=130,y=100)
    
    fl2 =Label(ffpas,text="كلمة المرور   ",bg="black",fg="white",font=("Arial",15))
    fl2.place(x=550,y=200)
        
    fe2=Entry(ffpas,width=60)
    fe2.place(x=130,y=200)
    

    
    def auth():
        fe11=fe1.get()
        fe22=fe2.get()
        
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        #con = mysql.connect(host="localhost", user="root", password="", database='database')
        cur = con.cursor()
        
        cur.execute("SELECT DISTINCT passwordt FROM users WHERE email=%s   ORDER BY email ASC", (fe11,))
        out = (cur.fetchone()[0])
        
        
        if (fe22==out):
            login_doctors()
        else:
            MessageBox.showinfo("ok","كلمة المرور خطأ")
            
            
            
    fb1 = Button(ffpas,text="التالي ",width=40,bg="black",fg="white",font=("Arial",15),command=auth)
    fb1.place(x=100,y=400)





def updateinfodoctor():
    f_updateinfodoctor = Frame(root,width=700,height=550,bg=bkg)
    f_updateinfodoctor.place(x=0,y=50)

    l1_updateinfodoctor = Label(f_updateinfodoctor,text="ادخل ايميلك",bg="black",fg="white",font=("Arial",15))
    l1_updateinfodoctor.place(x=530,y=50)
    e1_updateinfodoctor = Entry(f_updateinfodoctor,width=40)
    e1_updateinfodoctor.place(x=5,y=50)

    def deletdoctor():
        e1valu = str(e1_updateinfodoctor.get())
        if (e1valu ==""):
            MessageBox.showinfo("field")
        else:
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con = mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='sql12623107')
            #con = mysql.connect(host="localhost",user="root",password="",database='database')
            cur = con.cursor()
            cur.execute('DELETE FROM `doctors` WHERE email=%s',(e1valu,))
            MessageBox.showinfo("sucsess delete")
            con.commit()
            con.close()


    b1_updateinfodoctor=Button(f_updateinfodoctor,text="حذف حسابي",bg="black",fg="white",width=20,cursor="hand2",command=deletdoctor,font=("Arial",15))
    b1_updateinfodoctor.place(x=100,y=100)
    l2_updateinfodoctor = Label(f_updateinfodoctor,text="مالذي تريد تعديله ",bg="black",fg="white",font=("Arial",15))
    l2_updateinfodoctor.place(x=530,y=150)

    options =["الاسم الكامل","الاختصاص","ايام المشفى","ايام العيادة","ساعات العمل"]
    e3_updateinfodoctor =ttk.Combobox(root, values=options,state="readonly",font=("Arial",15))
    e3_updateinfodoctor.place(x=50,y=200)

    l3_updateinfodoctor = Label(f_updateinfodoctor,text="البيانات الجديدة",bg="black",fg="white",font=("Arial",15))
    l3_updateinfodoctor.place(x=530,y=300)

    e2_updateinfodoctor = Entry(f_updateinfodoctor,width=70)
    e2_updateinfodoctor.place(x=5,y=300)

    def updatedata():
        em = str(e1_updateinfodoctor.get())
        eup = e3_updateinfodoctor.get()
        enew = e2_updateinfodoctor.get()
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        #con = mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='sql12623107')
        #con = mysql.connect(host="localhost", user="root", password="", database='database')
        cur = con.cursor()
        if (em =="" or eup =="" or enew ==""):
            MessageBox.showinfo("field")
        elif (eup == "الاختصاص"):
            cur.execute('UPDATE `doctors` SET work=%s WHERE email=%s ',(enew,em))
            con.commit()
            MessageBox.showinfo("success")
            con.close()

        elif (eup == "الاسم الكامل"):
            cur.execute('UPDATE `doctors` SET fullname=%s WHERE email=%s ', (enew, em))
            con.commit()
            MessageBox.showinfo("success")
            con.close()

        elif (eup == "ايام المشفى"):
            cur.execute('UPDATE `doctors` SET dayinhospital=%s WHERE email=%s ', (enew, em))
            con.commit()
            MessageBox.showinfo("success")
            con.close()

        elif (eup == "ايام العيادة"):
            cur.execute('UPDATE `doctors` SET dayinhome=%s WHERE email=%s ', (enew, em))
            con.commit()
            MessageBox.showinfo("success")
            con.close()

        elif (eup == "ساعات العمل"):
            cur.execute('UPDATE `doctors` SET hourofwork=%s WHERE email=%s ', (enew, em))
            con.commit()
            MessageBox.showinfo("success")
            con.close()


    b2_updateinfodoctor=Button(f_updateinfodoctor,text="تحديث",bg="black",fg="white",width=20,cursor="hand2",command=updatedata,font=("Arial",15))
    b2_updateinfodoctor.place(x=40,y=350)







def pas2():
    
    fpas = Frame(root,width=700,height=550,)
    fpas.place(x=0,y=50)
    
    l1 =Label(fpas,text="الايميل   ",bg="black",fg="white",font=("Arial",15))
    l1.place(x=550,y=100)
        
    e1=Entry(fpas,width=60)
    e1.place(x=130,y=100)
    
    l2 =Label(fpas,text="كلمة المرور   ",bg="black",fg="white",font=("Arial",15))
    l2.place(x=550,y=200)
        
    e2=Entry(fpas,width=60)
    e2.place(x=130,y=200)
    
    
    
    def auth():
        e11=e1.get()
        e22=e2.get()
        
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        #con = mysql.connect(host="localhost", user="root", password="", database='database')
        cur = con.cursor()
        
        cur.execute("SELECT DISTINCT passwordt FROM users WHERE email=%s   ORDER BY email ASC", (e11,))
        out = (cur.fetchone()[0])
        
        
        if (e22==out):
            updateinfodoctor()
        else:
            MessageBox.showinfo("ok","كلمة المرور خطأ")
            
        
        
    
    
    
    
    
    
    b1 = Button(fpas,text="التالي ",width=40,bg="black",fg="white",font=("Arial",15),command=auth)
    b1.place(x=100,y=400)
    







def doctor():
    backk()
    fdoctor =Frame(root,width=190,height=550)
    fdoctor.place(x=800,y=50)
    
    image3 = Image.open("C:\\Users\\ASUS\\Desktop\\6.jpeg")
    image3=image3.resize((700,590))
    test = ImageTk.PhotoImage(image3)

    label1 = Label(root,image=test)
    label1.image = test

    label1.place(x=0,y=50)
    
    def hide():
        fdoctor =Frame(root,width=190,height=550)
        fdoctor.place(x=800,y=50)
        

        

    b11doctor = Button(fdoctor,height=2,text="❌",fg="black",font=("Arial",15),command=hide)
    b11doctor.place(x=100,y=0)
    
    b1doctor = Button(fdoctor,width=15,height=2,text="اضافة بياناتي  ",fg="black",font=("Arial",15),command=pas3)
    b1doctor.place(x=0,y=100)
    
    b2doctor = Button(fdoctor,width=15,height=2,text=" تعديل بياناتي",fg="black",font=("Arial",15),command=pas2)
    b2doctor.place(x=0,y=300)
        
def mapp():
    webbrowser.open('https://www.google.com/maps/@34.7648965,36.5891838,8z?entry=ttu')


def google():
    webbrowser.open('https://accounts.google.com/signin/v2/challenge/pwd?TL=AG7eRGAsbhGy8l84qfiGzyn04m2xa2S82XMPjmgOI6RjcLBA87d1WO0rC25WMqyc&cid=1&continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&flowName=GlifWebSignIn&ifkv=Af_xneFfXdspJZgeOH4H5p9gk5bB-yUD6AQKzofV0jiFQoVLbfNeUxoxh4E_iolzSDRQLjohzJkz&rart=ANgoxccMVlQ9zv_KjPMBIpgkeEE1NbSU6fanpYZ7POlT9QasNXz-Te_TwOFhxfKgj9A_maFB8bUMuaMd7WxZwCiLrwlZy0SQ3g&sarp=1&scc=1&service=accountsettings&flowEntry=ServiceLogin')



def page2():
    f_page2 = Frame(root,width=700,height=550,bg=bkg)
    f_page2.place(x=0,y=50)

    l_page2 = Label(f_page2,text="للحصول على كلمة مرور اتبع التعليمات التالية",bg=bkg,fg="black",font=("Arial",15))
    l_page2.place(x=20,y=10)

    l1_page2 = Label(f_page2,text="-1 قم بتفعيل ميزة التحقق بخطوتين لتأمين حسابك ",bg=bkg,fg="white",font=("Arial",15))
    l1_page2.place(x=10,y=50)
    def helpp():
        f_help=Frame(root,width=700,height=550,bg=bkg,)
        f_help.place(x=0,y=50)


        l1=Label(f_help,text=" ⬅انتقل اللى حسابك  ",bg=bkg,font=("Arial",15))
        l1.place(x=100,y=20)
        l2=Label(f_help,text=" ⬅ادارة حسابك على غوغل  ",bg=bkg,font=("Arial",15))
        l2.place(x=100,y=70)
        l3=Label(f_help,text=" ⬅الامان  ",bg=bkg,font=("Arial",15))
        l3.place(x=100,y=120)
        l3=Label(f_help,text=" ⬅التحقق بخطوتين  ",bg=bkg,font=("Arial",15))
        l3.place(x=100,y=170)
        l4=Label(f_help,text=" ⬅البدء  ",bg=bkg,font=("Arial",15))
        l4.place(x=100,y=210)
        l5=Label(f_help,text=" ⬅ادخل رقم هاتف خاص بك  ",bg=bkg,font=("Arial",15))
        l5.place(x=100,y=260)
        l6=Label(f_help,text=" ⬅ادخل الرمز  ",bg=bkg,font=("Arial",15))
        l6.place(x=100,y=310)
        l7=Label(f_help,text=" ⬅تفعيل  ",bg=bkg,font=("Arial",15))
        l7.place(x=100,y=360)

        b_helpp=Button(f_help,width=40,text="عودة",bg="black",fg="white",cursor="hand2",command=page2,font=("Arial",15))
        b_helpp.place(x=5,y=500)



    b2_page2 = Button(f_page2,text="مساعدة",width=5,bg="black",fg="white",cursor="hand2",command=helpp,font=("Arial",15))
    b2_page2.place(x=100,y=100)

    l2_page2 = Label(f_page2,text="-2 ادخل ايميلك وكلمة المرور ",bg=bkg,fg="white",font=("Arial",15))
    l2_page2.place(x=50,y=150)
    l3_page2 = Label(f_page2,text="-3 في خيار select app اختر mail ",bg=bkg,fg="white",font=("Arial",15))
    l3_page2.place(x=50,y=180)
    l4_page2 = Label(f_page2,text="-4 حدد الجهاز ",bg=bkg,fg="white",font=("Arial",15))
    l4_page2.place(x=50,y=210)
    l5_page2 = Label(f_page2,text="-5 اضغط على انشاء واحتفظ بكلمة المرور ",bg=bkg,fg="white",font=("Arial",15))
    l5_page2.place(x=50,y=240)
    l6_page2 = Label(f_page2,text="-6 اضغط على التالي وقم بتعبئة المطلوب ",bg=bkg,fg="white",font=("Arial",15))
    l6_page2.place(x=50,y=270)

    b1_page2 = Button(f_page2,text="الحصول على كلمة المرور",width=50,bg="black",fg="white",cursor="hand2",command=google,font=("Arial",15))
    b1_page2.place(x=0,y=390)










def getpassword():
    f_getpassword = Frame(root,width=700,height=550,bg=bkg)
    f_getpassword.place(x=0,y=50)

    l_getpassword = Label(f_getpassword,text="احصل على كلمة مرور خاصة بك لتستخدمها في التطبيق",bg=bkg,fg="white",font=("Arial",15))
    l_getpassword.place(x=30,y=50)



    b2_getpassword = Button(f_getpassword,text="ليس لدي كلمة مرور بعد",bg="black",fg="white",width=60,cursor="hand2",command=page2,font=("Arial",15))
    b2_getpassword.place(x=0,y=200)



def great_account():
    ca = Frame(root,width=700,height=550,bg=bkg)
    ca.place(x=0,y=50)
    

    

    l1_ca = Label(ca,text="الاسم الكامل ",bg="black",fg="white",font=("Arial",15))
    l1_ca.place(x=600,y=50)
    e1_ca = Entry(ca,width=50  )
    e1_ca.place(x=20,y=50)
    
    
    l2_ca = Label(ca,text="الايميل  ",bg="black",fg="white",font=("Arial",15))
    l2_ca.place(x=600,y=100)
    e2_ca = Entry(ca,width=50  )
    e2_ca.place(x=20,y=100)
    

    l3_ca= Label(ca,text="كلمة المرور ",bg="black",fg="white",font=("Arial",15))
    l3_ca.place(x=600,y=150)
    e3_ca = Entry(ca,width=50)
    e3_ca.place(x=20,y=150)
    
    
    
    def add():
        e1 = e1_ca.get()
        e2 = e2_ca.get()
        e3 = e3_ca.get()


        if (e1=="" or e2=="" or e3==""):
            MessageBox.showinfo("الحقول مطلوبه")
        else:
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con=mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='sql12623107')
            #con = mysql.connect(host="localhost",user="root",password="",database='database')
            cur = con.cursor()
            query = 'INSERT INTO `users`(`fullname`, `email` ,`password`,`passwordt` ) VALUES(%s,%s,%s,%s)'
            val = (e1,e2,e3," ")
            cur.execute(query, val)
            e1_ca.delete(0,END)
            e2_ca.delete(0,END)
            e3_ca.delete(0,END)


            MessageBox.showinfo("✔", "تمت العملية بنجاح")
            con.commit()
            con.close()


    b1_login_doctors = Button(ca,text="ارسال",width=40,bg="black",fg="white",cursor="hand2",command=add)
    b1_login_doctors.place(x=5,y=350)







def great_account_d():
    ca = Frame(root,width=700,height=550,bg=bkg)
    ca.place(x=0,y=50)
    

    

    l1_ca = Label(ca,text="الاسم الكامل ",bg="black",fg="white",font=("Arial",15))
    l1_ca.place(x=550,y=50)
    e1_ca = Entry(ca,width=50  )
    e1_ca.place(x=20,y=50)
    
    
    l2_ca = Label(ca,text="الايميل  ",bg="black",fg="white",font=("Arial",15))
    l2_ca.place(x=550,y=100)
    e2_ca = Entry(ca,width=50  )
    e2_ca.place(x=20,y=100)
    

    l3_ca= Label(ca,text=" كلمة مرولا التطبيق",bg="black",fg="white",font=("Arial",15))
    l3_ca.place(x=550,y=150)
    e3_ca = Entry(ca,width=50)
    e3_ca.place(x=20,y=150)
    
    
    l4_ca= Label(ca,text=" كلمة مرور الخدمات",bg="black",fg="white",font=("Arial",15))
    l4_ca.place(x=550,y=200)
    e4_ca = Entry(ca,width=50)
    e4_ca.place(x=20,y=200)
    
    
    def add():
        e1 = e1_ca.get()
        e2 = e2_ca.get()
        e3 = e3_ca.get()
        e4 = e4_ca.get()


        if (e1=="" or e2=="" or e3=="" or e4==""):
            MessageBox.showinfo("الحقول مطلوبه")
        else:
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            #con=mysql.connect(host="sql12.freesqldatabase.com", user="sql12623107", password="4YP8kzFt9H", database='sql12623107')
            #con = mysql.connect(host="localhost",user="root",password="",database='database')
            cur = con.cursor()
            query = 'INSERT INTO `users`(`fullname`, `email` ,`password`,`passwordt` ) VALUES(%s,%s,%s,%s)'
            val = (e1,e2,e3,e4)
            cur.execute(query, val)
            e1_ca.delete(0,END)
            e2_ca.delete(0,END)
            e3_ca.delete(0,END)
            e4_ca.delete(0,END)


            MessageBox.showinfo("✔", "تمت العملية بنجاح")
            con.commit()
            con.close()


    b1_login_doctors = Button(ca,text="ارسال",width=40,bg="black",fg="white",cursor="hand2",command=add)
    b1_login_doctors.place(x=5,y=350)







def other():
    fdoctor =Frame(root,width=190,height=550)
    fdoctor.place(x=800,y=50)
    
    def hide():
        fdoctor =Frame(root,width=190,height=550)
        fdoctor.place(x=800,y=50)
        

        

    b11doctor = Button(fdoctor,height=2,text="❌",fg="black",font=("Arial",15),command=hide)
    b11doctor.place(x=100,y=0)
    
    b1doctor = Button(fdoctor,width=15,height=2,text=" كلمة المرور ",fg="black",font=("Arial",15),command=getpassword)
    b1doctor.place(x=0,y=100)
    
    b2doctor = Button(fdoctor,width=15,height=2,text="  اضافة حسابي مستخدم",fg="black",font=("Arial",15),command=great_account)
    b2doctor.place(x=0,y=200)
    
    b3doctor = Button(fdoctor,width=15,height=2,text="  اضافة حسابي طبيب",fg="black",font=("Arial",15),command=great_account_d)
    b3doctor.place(x=0,y=300)
    
    
    

def finsh():
    root.destroy()  
         
def emer():
    MessageBox.showinfo("تنبيه", "رمز الطوارئ الخاص بالإسعاف هو 110")

def first():
    bmain = Button(root,text="الصفحة الرئيسية",width=15,bg="blue",fg="white",command=mainn,font=("Arial",15))
    bmain.place(x=0,y=0)

    bmain2 = Button(root,text="طبيب",width=15,bg="black",fg="white",font=("Arial",15),command=doctor)
    bmain2.place(x=200,y=0)

    bmain3 = Button(root,text="مريض",width=15,bg="black",fg="white",font=("Arial",15),command=customer)
    bmain3.place(x=400,y=0)

    bmain3 = Button(root,text="المزيد",width=15,bg="black",fg="white",font=("Arial",15),command=other)
    bmain3.place(x=600,y=0)

    bmain4 = Button(root,text="الخريطة",width=40,bg="black",fg="white",font=("Arial",15),command=mapp)
    bmain4.place(x=520,y=650)

    bmain5 = Button(root,text="الطوارئ",width=40,bg="red",fg="white",font=("Arial",15),command=emer)
    bmain5.place(x=0,y=650)
    
    bb3 = Button(root,width=15,text="اغلاق التطبيق",bg="red",fg="white",command=finsh,font=("Arial",15))
    bb3.place(x=800,y=0)



def p1():

    image1 = Image.open("C:\\Users\\ASUS\\Desktop\\6.jpeg")
    image1=image1.resize((1000,700))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    label1.place(x=0,y=0)
    
    def start():
       
        fstart = Frame(root,width=1000,height=600,)
        fstart.place(x=0,y=40)
        image2 = Image.open("C:\\Users\\ASUS\\Desktop\\6.jpeg")
        image2=image2.resize((1000,600))
        test = ImageTk.PhotoImage(image2)

        label1 = Label(fstart,image=test)
        label1.image = test

        label1.place(x=0,y=0)
        
        
        first()
    def finsh():
        root.destroy()  
          
    
    bb = Button(root,width=30,text="ابدأ",bg="black",fg="white",height=2,command=start)
    bb.place(x=100,y=500)
    
    bb2 = Button(root,width=30,text="اغلاق التطبيق",bg="black",fg="white",height=2,command=finsh)
    bb2.place(x=650,y=500)
    root.mainloop()

p1()

root.mainloop()