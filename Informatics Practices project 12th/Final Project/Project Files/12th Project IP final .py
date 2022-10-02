import mysql.connector as sqlt
import matplotlib.pyplot as mt
import pandas as pd
con=sqlt.connect(host='localhost',user='root',passwd='ojasaklecha',database='ip')
#outside window
#register
def register():
    cur=con.cursor()
    print("1. Register as Admin")
    print("2. Register as Student")
    c3=int(input("Enter your choice : "))
    if c3==1:
        x=str(input('Enter your Name :'))
        print('-'*60)
        y=str(input('Create Username :'))
        print('-'*60)
        z=str(input('Create Password :'))
        print('-'*60)
        cur.execute("insert into alogins values('%s','%s','%s')"%(x,y,z))
        con.commit()
    else:
        x=str(input('Enter your Name :'))
        print('-'*60)
        y=str(input('Create Username :'))
        print('-'*60)
        z=str(input('Create Password :'))
        print('-'*60)
        cur.execute("insert into logins values('%s','%s','%s')"%(x,y,z))
        con.commit()
#adminfunctions
#searchkaro
def searchkaro():
    c1='y'
    while (c1=='y' or c1=='Y'):
        cur=con.cursor()
        print("1. Name \n2. Gender \n3. Year of Admission \n4. 12th Percentage \n5. Branch")
        cho=int(input("enter your choice : "))
        if cho==1:
            x=input("Enter the name : ")
            quer=("select * from college_admission where name='%s';" %x)
            cur.execute(quer)
            row=cur.fetchall()
            for z in row:
                print(z)
                print('*'*60)
                break
            else:
                print('No Record Found...')

        if cho==2:
            print("Gender - \n1. Male \n2. Female \n3. Others")
            x=input("Enter the Gender(type) : ")
            quer=("select * from college_admission where gender='%s';" %x)
            cur.execute(quer)
            row=cur.fetchall()
            for z in row:
                print(z)
            else:
                print('No Record Found...')
            print('*'*60)
        if cho==3:
            x=int(input("Enter the Year of Admission : "))
            quer=("select * from college_admission where year_of_admission=%s;" %x)
            cur.execute(quer)
            row=cur.fetchall()
            for z in row:
                print(z)
            else:
                print('No Record Found...')
            print('*'*60)
        if cho==4:
            x=int(input("Enter the 12th Percentage : "))
            quer=("select * from college_admission where 12th_Board_percentage='%s';" %x)
            cur.execute(quer)
            row=cur.fetchall()
            for z in row:
                print(z)
            else:
                print('No Record Found...')
            print('*'*60)
        if cho==5:
            print("Branchs - \n1. computer science \n2. electronics \n3. mechanical")
            x=str(input("Enter the Branch(type) : "))
            quer=("select * from college_admission where branch='%s';" %x)
            cur.execute(quer)
            row=cur.fetchall()
            for z in row:
                print(z)
            else:
                print('No Record Found...')
            print('*'*60)
        c1=input("Want to continue using function ? : press y for yes and press n for no : ")
            
#displaykaro
def displaykaro():
    c1='y'
    while (c1=='y' or c1=='Y'):
        print('1. Tabular')
        print('2. Graphical')
        x=int(input('Select option to input : '))
        if x==1 :
            print('*'*60)
            print("DISPLAY RECORDS IN TABULAR FORM")
            print('*'*60)
            cur=con.cursor()
            cur.execute("select * from college_admission")
            data=cur.fetchall()
            for row in data:
                print(row)
            print('*'*60)
        
        elif x==2:
            print('1. Year Wise')
            print('2. Branch Wise')
            print('3. Gender Wise')
            y=int(input('Select option to input : '))
            if y==1:
                df=pd.read_sql('select year_of_admission,count(*) from college_admission group by year_of_admission',con)
                mt.bar(df['year_of_admission'],df['count(*)'])
                mt.xlabel('Year')
                mt.ylabel('Number of Students')
                mt.title('Year Wise admission of number of students')
                mt.show()
            elif y==2:
                df=pd.read_sql('select branch,count(*) from college_admission group by branch',con)
                mt.bar(df['branch'],df['count(*)'])
                mt.xlabel('Branch')
                mt.ylabel('Number of Students')
                mt.title('Branch Wise admission of number of students')
                mt.show()
            elif y==3:
                df=pd.read_sql('select gender,count(*) from college_admission group by gender',con)
                mt.bar(df['gender'],df['count(*)'])
                mt.xlabel('Gender')
                mt.ylabel('Number of Students')
                mt.title('Gender Wise admission of number of students')
                mt.show()
        c1=input("Want to continue using function ? : press y for yes and press n for no : ")
#deletekaro
def deletekaro():
    c1='y'
    while (c1=='y' or c1=='Y'):
        print('*'*60)
        print("DELETE RECORDS")
        print('*'*60)
        cur=con.cursor()
        cur.execute("select * from college_admission")
        data=cur.fetchall()
        for row in data:
            print(row)
        print('*'*60)
        d=(input("ENTER NAME OF STUDENT WANTS TO DELETE : "))
        print('*'*60)
        cur=con.cursor()
        cur.execute("select name from college_admission")
        data=cur.fetchall()
        c=0
        for row in data:
            if row[0]==d:
                c=1
                break
        if c==0:
            print("Record not found")
        else:
            cur.execute("delete from college_admission where name='%s'"%d)
            con.commit()
            print("Record deleted successfully.....")
        c1=input("Want to continue using function ? : press y for yes and press n for no : ")
#updatekaro
def updatekaro():
    c1='y'
    while (c1=='y' or c1=='Y'):
        print('*'*60)
        print("UPDATE RECORDS")
        print('*'*60)   
        cur=con.cursor()
        cur.execute("select * from college_admission")
        data=cur.fetchall()
        for row in data:
            print(row)
        print('*'*60)
        a=input("ENTERS NAME STUDENT WANTS TO CHANGE : ")
        print('*'*60)
        cur=con.cursor()
        cur.execute("select name from college_admission")
        data=cur.fetchall()
        c=0
        for row in data:
            if row[0]==a:
                c=1
                break
        if c==0:
            print("Record not found")
        else:
            d=input("ENTER NEW STUDENT NAME : ")
            e=input("ENTER NEW DATE OF BIRTH(DD-MM-YYYY) : ")
            h=input('ENTER NEW GENDER : ')
            g=int(input('ENTER NEW YEAR OF ADMISSION(YYYY) : '))
            f=int(input("ENTER NEW 12TH PERCENTAGE : "))
            if f>=75 and f<80:
                print('^'*60)
                print('You can opt only Electronics')
                print('^'*60)
                cur=con.cursor()
                cur.execute("update college_admission set name='%s',dob='%s',gender='%s',year_of_admission=%s,12th_Board_percentage=%s,branch='%s' where name='%s'"%(d,e,h,g,f,'Electronics',a))
                con.commit()
                print("Record updated successfully...")
            elif f>=80 and f<85 :
                print('^'*60)
                print('You can opt Electronics or Mechanical')
                print('^'*60)
                ao=(input('ENTER NEW SUBJECT : '))
                cur=con.cursor()
                cur.execute("update college_admission set name='%s',dob='%s',gender='%s',year_of_admission=%s,12th_Board_percentage=%s,branch='%s' where name='%s'"%(d,e,h,g,f,ao,a))
                con.commit()
                print("Record updated successfully...")
            elif f>=85 and f<=100:
                print('^'*60)
                print('You can opt Electronics or Mechanical or Computer Science')
                print('^'*60)
                ao=(input('ENTER NEW SUBJECT : '))
                cur=con.cursor()
                cur.execute("update college_admission set name='%s',dob='%s',gender='%s',year_of_admission=%s,12th_Board_percentage=%s,branch='%s' where name='%s'"%(d,e,h,g,f,ao,a))
                con.commit()
                print('Records updated successfully...')
            c1=input("Want to Continue using function ? : press y for yes and press n for no : ")    
#adminpresentation
def adminlogin():
    c='y'
    while (c=='y' or c=='Y'):
        print('='*60)
        print("WELCOME TO ADMIN DASHBOARD")
        print('='*60)
        print("1. DISPLAY STUDENT LIST")
        print("2. UPDATE STUDENT RECORD")
        print("3. DELETE STUDENT RECORD")
        print("4. SEARCH STUDENT DETAILS")
        print('#'*60)
        c2=int(input("Enter your choice : "))
        if c2==1:
            displaykaro()
        elif c2==2:
            updatekaro()
        elif c2==3:
            deletekaro()
        elif c2==4:
            searchkaro()
        else:
            print('Wrong Choice Entered')
            print('='*60)
        print('+'*60)
        c=input("Do you want to continue in the portal ? : press y for yes and press n for no : ")
        print('+'*60)

#login
def alogin():
    cur=con.cursor()
    cur.execute("select UserName,password from alogins")
    data=cur.fetchall()
    x=input('Enter your username : ')
    y=input('Enter your password : ')
    for row1,row2 in data:
        if x==row1 and y==row2:
            print('*'*60)
            print("Login successfully...")
            print('*'*60)
            adminlogin()
            break
    else:
        print('*'*60)
        print("Wrong credentials...")
        print('*'*60)

#userfuntions
def userlogin():
#display records
    def display():
        c1='y'
        while(c1=='y' or c1=='Y'):
            print('*'*60)
            print("DISPLAY RECORDS")
            print('*'*60)
            e=input('ENTER YOUR NAME AS PER RECORD : ')
            cur=con.cursor()
            cur.execute("select * from college_admission where name='%s'"%e)
            data=cur.fetchall()
            for row in data:
                print(row)
            print('*'*60)
            c1=input("Want to continue: press y for yes and press n for no : ")
            print('*'*60)
#insert records
    def insert():
        c1='y'
        while(c1=='y' or c1=='Y'):
            print('*'*80)
            print("NEW ADMISSION")
            print('*'*80)
            d=str(input('enter your name : '))
            print('*'*80)
            e=str(input('enter your dob(DD-MM-YYYY) : '))
            print('*'*80)
            h=str(input('enter your gender(Male/Female/Others) : '))
            print('*'*80)
            g=str(input('enter the year of admission(YYYY) : '))
            print('*'*80)
            f=float(input('enter your 12th boards percentage : '))
            print('*'*80)
            if f>=75 and f<80 :
                print('you can choose ELECTRONICS as your branch')
                y=(input('Do you want to take (y/n) : '))
                print('*'*80)
                if y=='y' or y=='Y' or y=='yes' or y=='Yes' :
                    cur=con.cursor()
                    cur.execute("insert into college_admission values('%s','%s','%s','%s','%s','%s')"%(d,e,h,g,f,'ELECTRONICS'))
                    con.commit()
                    print('whohooooo you are the part of our family.....')
                else :
                    print('Sorry ! about that....')
            elif f>=80 and f<85:
                print('You can choose MECHANICAL or ELECTRONICS as your Branch')
                ok=(input('do you want to take (y/n) : '))
                if ok=='y' or ok=='Y' or ok=='yes' or ok=='Yes' :
                    u=(input('Which branch you want to choose : '))
                    if u=='mechanical' or u=='electronics' or u=='Mechanical' or u=='Electronics':
                        cur=con.cursor()
                        cur.execute("insert into college_admission values('%s','%s','%s','%s','%s','%s')"%(d,e,h,g,f,u))
                        con.commit()
                        print('whohooooooo you are the part of our family')
                    else :
                        print('Sorry about that.......')
                else:
                    print('thanks for your concern')
            elif f>=85 and f<=100:
                print('You can choose ELECTRONICS or MECHANICAL or COMPUTER SCIENCE')
                j=(input('Do you want to take (y/n) : '))
                if j=='y' or j=='Y' or j=='yes' or j=='Yes':
                    v=(input('Which branch you want to take : '))
                    if v=='mechanical' or v=='electronics' or v=='Mechanical' or v=='Electronics' or v=='Computer Science' or v=='computer science':
                        cur=con.cursor()
                        cur.execute("insert into college_admission values('%s','%s','%s','%s','%s','%s')"%(d,e,h,g,f,v))
                        con.commit()
                        print('whohoooooo you are the part of our family.....')
                    else :
                        print('thanks for concern')
                else:
                    print('thanks for concern')
            elif f<75 :
                print('Sorry you can not be enrolled.....')
            elif f>100 and f<=0 :
                print('NoWay It is Not Possible')
            print('*'*80)    
            c1=input("Want to Continue ? : press y for yes and press n for no : ")

#delete records
    def delete():
        c1='y'
        while (c1=='y' or c1=='Y'):
            print('*'*60)
            print("DELETE RECORDS")
            print('*'*60)
            cur=con.cursor()
            cur.execute("select * from college_admission")
            data=cur.fetchall()
            for row in data:
                print(row)
            print('*'*60)
            d=(input("ENTER NAME OF STUDENT WANTS TO DELETE : "))
            print('*'*60)
            cur=con.cursor()
            cur.execute("select name from college_admission")
            data=cur.fetchall()
            c=0
            for row in data:
                if row[0]==d:
                    c=1
                    break
            if c==0:
                print("Record not found")
            else:
                cur.execute("delete from college_admission where name='%s'"%(d))
                con.commit()
                print("Record deleted successfully.....")
            c1=input("Want to continue ? : press y for yes and press n for no : ")
#update records
    def update():
        c1='y'
        while (c1=='y' or c1=='Y'):
            print('*'*60)
            print("UPDATE RECORDS")
            print('*'*60)   
            cur=con.cursor()
            cur.execute("select * from college_admission")
            data=cur.fetchall()
            for row in data:
                print(row)
            print('*'*60)
            a=(input("ENTERS NAME STUDENT WANTS TO CHANGE : "))
            print('*'*60)
            cur=con.cursor()
            cur.execute("select name from college_admission")
            data=cur.fetchall()
            c=0
            for row in data:
                if row[0]==a:
                    c=1
                    break
            if c==0:
                print("Record not found")
            else:
                d=input("ENTER NEW STUDENT NAME : ")
                e=input("ENTER NEW DATE OF BIRTH (DD-MM-YYYY) : ")
                g=input('ENTER NEW YEAR OF ADMISSION(YYYY) : ')
                f=float(input("ENTER NEW 12TH PERCENTAGE : "))
                h=str(input('ENTER YOUR GENDER(MALE/FEMALE/OTHERS) : '))
                if f>=75 and f<80:
                    cur=con.cursor()
                    cur.execute("update college_admission set name='%s',dob='%s',gender='%s',year_of_admission=%s,12th_Board_percentage=%s,branch='%s' where name='%s'"%(d,e,h,g,f,'Electronics',a))
                    con.commit()
                    print("Record updated successfully...")
                elif f>=80 and f<85 :
                    ao=(input('what is your current branch : '))
                    n=input("Enter new branch : Electrical or Mechanical : ")
                    if ao=='Electronics' or ao=='electronics':
                        cur=con.cursor()
                        cur.execute("update college_admission set name='%s',dob='%s',gender='%s',year_of_admission=%s,12th_Board_percentage=%s,branch='%s' where name='%s'"%(d,e,h,g,f,'Electrical',a))
                        con.commit()
                        print("Record updated successfully...")
                    elif ao=='Mechanics' or ao=='mechanics':
                        cur=con.cursor()
                        cur.execute("update college_admission set name='%s',dob='%s',gender='%s',year_of_admission=%s,12th_Board_percentage=%s,branch='%s' where name='%s'"%(d,e,h,g,f,'Mechanical',a))
                        con.commit()
                        print("Record updated successfully...")
                elif f>=85 and f<=100:
                    ao=(input('what is your current branch : '))
                    jai=(input('Enter you new branch : Electrical or Mechanical or Computer Science : '))
                    cur=con.cursor()
                    cur.execute("update college_admission set name='%s',dob='%s',gender='%s',year_of_admission=%s,12th_Board_percentage=%s,branch='%s' where name='%s'"%(d,e,h,g,f,jai,a))
                    con.commit()
                    print("Record updated successfully...")     
            c1=input("Want to Continue ? : press y for yes and press n for no : ")
#userpresentation
    c='y'
    while (c=='y' or c=='Y'):
        print('*'*60)
        print("          USER LOGIN PORTAL")
        print('*'*60)
        print("         1. NEW ADMISSION")
        print("         2. DISPLAY RECORDS")
        print("         3. DELETE YOUR RECORD")
        print("         4. UPDATE RECORD")
        ch=int(input("Enter your choice : "))
        if ch==1:
            insert()
        if ch==2:
            display()
        if ch==3:
            delete()
        if ch==4:
            update()
        if ch>=5:
            print("wrong choice entered")
            print('*'*60)
        c=input("Do you want to continue in the portal ? : press y for yes and press n for no : ")
    else:
        print('*'*60)
        print("        Have a nice day!")
        print('*'*60)
            

#userloginpresentation
def ulogin():
    cur=con.cursor()
    cur.execute("select UserName,password from logins")
    data=cur.fetchall()
    x=input('Enter your username : ')
    y=input('Enter your password : ')
    for row1,row2 in data:
        if x==row1 and y==row2:
            print('*'*60)
            print("Login successfully...")
            print('*'*60)
            userlogin()
            break
    else:
        print('*'*60)
        print("Wrong credentials...")
        print('*'*60)


#outerpresentation
c='n'
while (c=='n' or c=='N'):
    print('-'*60)
    print('Welcome To XYZ College')
    print('-'*60)
    print('1.Register')
    print('2.Login')
    print('+'*60)
    ch=int(input("Enter your choice : "))
    print('+'*60)
    if ch==1:
        print('*'*60)
        print('Welcome to the Registration Box')
        print('*'*60)
        register()
        print('You are Successfully Registered!!!')
    elif ch==2:
        z='n'
        while (z=='n' or z=='N'):
            print("1. Admin Login")
            print("2. User Login")
            print('-'*60)
            c1=int(input("Enter your choice : "))
            print('-'*60)
            if c1==1:
                alogin()
            elif c1==2:
                ulogin()
            else:
                print('Wrong Choice Entered')
                print('*'*60)
            z=input("Want to log out from login menu ? : press y for yes and press n for no : ")
            print('*'*60)
    else:
        print("wrong choice entered!!!")
        print('*'*60)
    c=input("Want to exit ? : press y for yes and press n for no : ")
else:
    print('*'*60)
    print("        Have a nice day!")
    print('*'*60)



