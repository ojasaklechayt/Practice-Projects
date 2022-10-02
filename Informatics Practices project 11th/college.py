import mysql.connector as mt
con=mt.connect(host="localhost",user="root",passwd="root",database="ip")
#insert records
def insert():
    c1='y'
    while(c1=='y' or c1=='Y'):
        print('*'*80)
        print("NEW ADMISSION")
        print('*'*80)
        d=str(input('enter your name :'))
        print('*'*80)
        e=str(input('enter your dob(DD-MM-YYYY):'))
        print('*'*80)
        f=float(input('enter your 12th boards percentage :'))
        print('*'*80)
        if f>=75 and f<80 :
            print('you can choose ELECTRONICS as your branch')
            y=(input('Do you want to take (y/n) :'))
            print('*'*80)
            if y=='y' or y=='Y' or y=='yes' or y=='Yes' :
                cur=con.cursor()
                cur.execute("insert into college_admission values('%s','%s','%s','%s')"%(d,e,f,'ELECTRONICS'))
                con.commit()
                print('whohooooo you are the part of our family.....')
            else :
                print('Sorry ! about that....')
        elif f>=80 and f<85 :
            print('You can choose MECHANICAL or ELECTRONICS as you Branch')
            ok=(input('do you want to take (y/n) :'))
            if ok=='y' or ok=='Y' or ok=='yes' or ok=='Yes' :
                u=(input('Which branch you want to choose :'))
                if u=='mechanical' or u=='electronics' or u=='Mechanical' or u=='Electronics':
                    cur=con.cursor()
                    cur.execute("insert into college_admission values('%s','%s','%s','%s')"%(d,e,f,u))
                    con.commit()
                    print('whohooooooo you are the part of our family')
                else :
                    print('Sorry about that.......')
            else:
                print('thanks for your concern')
        elif f>=85 and f<=100:
            print('You can choose ELECTRONICS or MECHANICAL or COMPUTER SCIENCE')
            j=(input('Do you want to take (y/n) :'))
            if j=='y' or j=='Y' or j=='yes' or j=='Yes':
                v=(input('Which branch you want to take :'))
                if v=='mechanical' or v=='electronics' or v=='Mechanical' or v=='Electronics' or v=='Computer Science' or v=='computer science':
                    cur=con.cursor()
                    cur.execute("insert into college_admission values('%s','%s','%s','%s')"%(d,e,f,v))
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
        c1=input("Want to insert more records: press y for yes and press n for no")
        
#display records
def display():
    print('*'*60)
    print("DISPLAY RECORDS")
    print('*'*60)
    cur=con.cursor()
    cur.execute("select * from college_admission")
    data=cur.fetchall()
    for row in data:
        print(row)
    print('*'*60)
    c1=input("Want to continue: press y for yes and press n for no")
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
            d=input("ENTER NEW STUDENT NAME: ")
            e=input("ENTER NEW DATE OF BIRTH: DD-MM-YYYY ")
            f=float(input("Enter New 12th percentage: "))
            if f>=75 and f<80:
                cur=con.cursor()
                cur.execute("update college_admission set name='%s',dob='%s',12th_Board_percentage='%s' where name='%s'"%(d,e,f,'Electronics'))
                con.commit()
                print("Record updated successfully...")
            elif f>=80 and f<85 :
                ao=(input('what is your current subject :'))
                if ao=='Electronics' or ao=='electronics':
                    cur=con.cursor()
                    cur.execute("update college_admission set name='%s',dob='%s',12th_Board_percentage='%s' where name='%s'"%(d,e,f,'Mechanics'))
                    con.commit()
                    print("Record updated successfully...")
                elif ao=='Mechanics' or ao=='mechanics':
                    cur=con.cursor()
                    cur.execute("update college_admission set name='%s',dob='%s',12th_Board_percentage='%s' where name='%s'"%(d,e,f,'Electronics'))
                    con.commit()
                    print("Record updated successfully...")
            elif f>=85 and f<=100:
                ao=(input('what is your current subject :'))
                if ao=='electronics' or ao=='Electronics':
                    jai=(input('Enter you new branch :'))
                    cur=con.cursor()
                    cur.execute("update college_admission set name='%s',dob='%s',12th_Board_percentage='%s' where name='%s'"%(d,e,f,jai))
                    con.commit()
                elif ao=='computer science' or ao=='Computer Science' :
                    jai=(input('Enter you new branch :'))
                    cur=con.cursor()
                    cur.execute("update college_admission set name='%s',dob='%s',12th_Board_percentage='%s' where name='%s'"%(d,e,f,jai))
                    con.commit()
                elif ao=='mechanics' or ao=='Mechanics':
                    jai=(input('Enter you new branch :'))
                    cur=con.cursor()
                    cur.execute("update college_admission set name='%s',dob='%s',12th_Board_percentage='%s' where name='%s'"%(d,e,f,jai))
                    con.commit()
        c1=input("Want to update more records : press y for yes and press n for no : ")
        
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
        c1=input("Want to delete more records : press y for yes and press n for no :")

#presentation
c='y'
while (c=='y' or c=='Y'):
    print('*'*60)
    print("          COLLEGE ADMISSION MANAGEMENT SYSTEM")
    print('*'*60)
    print("         1. NEW ADMISSION")
    print("         2. DISPLAY RECORDS")
    print("         3. UPDATE RECORD")
    print("         4. DELETE A RECORD")
    ch=int(input("Enter your choice : "))
    if ch==1:
        insert()
    if ch==2:
        display()
    if ch==3:
        update()
    if ch==4:
        delete()
    if ch>=5:
        print("wrong choice entered")
        print('*'*60)
    c=input("Want to continue to access our system : press y for yes and press n for no :")
else:
    print('*'*60)
    print("        Have a nice day!")
    print('*'*60)

    
    



