def searchkaro():
    print("1. Name \n2. Gender \n3. Year of Admission \n4. 12th Percentage \n5. Branch")
    cho=int(input("enter your choice : "))
    if cho==1:
        x=(input("Enter the name : "))
        quer=("select name from college_admission where name='%d';" %x)
        cur.execute(quer)
        row=cur.fetchall()
        lst=[]
        for z in row:
            for y in z:
                lst.append(y)
        quer1=("select dob from college_admission where name='%d';" %x) 
        cur.execute(quer1)
        row1=cur.fetchall()
        lst1=[]
        for z in row1:
            for y in z:
                lst1.append(y)
        quer2=("select gender from college_admission where name='%d';" %x)
        cur.execute(quer2)
        row2=cur.fetchall()
        lst2=[]
        for z in row2:
            for y in z:
                lst2.append(y)
        quer3=("select year_of_admission from college_admission where name='%d';" %x)
        cur.execute(quer3)
        row3=cur.fetchall()
        lst3=[]
        for z in row3:
            for y in z:
                lst3.append(y)
        quer4=("select 12th_Board_percentage from college_admission where name='%d';" %x)
        cur.execute(quer4)
        row4=cur.fetchall()
        lst4=[]
        for z in row4:
            for y in z:
                lst4.append(y)
        
        quer5=("select branch from college_admission where name='%d';" %x)
        cur.execute(quer5)
        row5=cur.fetchall()
        lst5=[]
        for z in row5:
            for y in z:
                lst5.append(y)
        ndf=pd.DataFrame({"Name":lst,"DOB":lst1,"Gender":lst2,"Year of admission":lst3,"12th Percentage":lst4,"Branch":lst5},index=[0])
        print(ndf)
        
        if cho==2:
        print("Gender - \n1. Male \n2. Female \n3. Others")
        x=(input("Enter the Gender : "))
        quer=("select name from college_admission where gender='%d';" %x)
        cur.execute(quer)
        row=cur.fetchall()
        lst=[]
        for z in row:
            for y in z:
                lst.append(y)
        quer1=("select dob from college_admission where gender='%d';" %x) 
        cur.execute(quer1)
        row1=cur.fetchall()
        lst1=[]
        for z in row1:
            for y in z:
                lst1.append(y)
        quer2=("select gender from college_admission where gender='%d';" %x)
        cur.execute(quer2)
        row2=cur.fetchall()
        lst2=[]
        for z in row2:
            for y in z:
                lst2.append(y)
        quer3=("select year_of_admission from college_admission where gender='%d';" %x)
        cur.execute(quer3)
        row3=cur.fetchall()
        lst3=[]
        for z in row3:
            for y in z:
                lst3.append(y)
        quer4=("select 12th_Board_percentage from college_admission where gender='%d';" %x)
        cur.execute(quer4)
        row4=cur.fetchall()
        lst4=[]
        for z in row4:
            for y in z:
                lst4.append(y)
        
        quer5=("select branch from college_admission where gender='%d';" %x)
        cur.execute(quer5)
        row5=cur.fetchall()
        lst5=[]
        for z in row5:
            for y in z:
                lst5.append(y)
        ndf=pd.DataFrame({"Name":lst,"DOB":lst1,"Gender":lst2,"Year of admission":lst3,"12th Percentage":lst4,"Branch":lst5},index=[0])
        print(ndf)
        
        if cho==3:
        x=(input("Enter the Year of Admission : "))
        quer=("select name from college_admission where year_of_admission='%d';" %x)
        cur.execute(quer)
        row=cur.fetchall()
        lst=[]
        for z in row:
            for y in z:
                lst.append(y)
        quer1=("select dob from college_admission where year_of_admission='%d';" %x) 
        cur.execute(quer1)
        row1=cur.fetchall()
        lst1=[]
        for z in row1:
            for y in z:
                lst1.append(y)
        quer2=("select gender from college_admission where year_of_admission='%d';" %x)
        cur.execute(quer2)
        row2=cur.fetchall()
        lst2=[]
        for z in row2:
            for y in z:
                lst2.append(y)
        quer3=("select year_of_admission from college_admission where year_of_admission='%d';" %x)
        cur.execute(quer3)
        row3=cur.fetchall()
        lst3=[]
        for z in row3:
            for y in z:
                lst3.append(y)
        quer4=("select 12th_Board_percentage from college_admission where year_of_admission='%d';" %x)
        cur.execute(quer4)
        row4=cur.fetchall()
        lst4=[]
        for z in row4:
            for y in z:
                lst4.append(y)
        
        quer5=("select branch from college_admission where year_of_admission='%d';" %x)
        cur.execute(quer5)
        row5=cur.fetchall()
        lst5=[]
        for z in row5:
            for y in z:
                lst5.append(y)
        ndf=pd.DataFrame({"Name":lst,"DOB":lst1,"Gender":lst2,"Year of admission":lst3,"12th Percentage":lst4,"Branch":lst5},index=[0])
        print(ndf)

        if cho==4:
        x=(input("Enter the 12th Percentage : "))
        quer=("select name from college_admission where 12th_Board_percentage='%d';" %x)
        cur.execute(quer)
        row=cur.fetchall()
        lst=[]
        for z in row:
            for y in z:
                lst.append(y)
        quer1=("select dob from college_admission where 12th_Board_percentage='%d';" %x) 
        cur.execute(quer1)
        row1=cur.fetchall()
        lst1=[]
        for z in row1:
            for y in z:
                lst1.append(y)
        quer2=("select gender from college_admission where 12th_Board_percentage='%d';" %x)
        cur.execute(quer2)
        row2=cur.fetchall()
        lst2=[]
        for z in row2:
            for y in z:
                lst2.append(y)
        quer3=("select year_of_admission from college_admission where 12th_Board_percentage='%d';" %x)
        cur.execute(quer3)
        row3=cur.fetchall()
        lst3=[]
        for z in row3:
            for y in z:
                lst3.append(y)
        quer4=("select 12th_Board_percentage from college_admission where 12th_Board_percentage='%d';" %x)
        cur.execute(quer4)
        row4=cur.fetchall()
        lst4=[]
        for z in row4:
            for y in z:
                lst4.append(y)
        
        quer5=("select branch from college_admission where 12th_Board_percentage='%d';" %x)
        cur.execute(quer5)
        row5=cur.fetchall()
        lst5=[]
        for z in row5:
            for y in z:
                lst5.append(y)
        ndf=pd.DataFrame({"Name":lst,"DOB":lst1,"Gender":lst2,"Year of admission":lst3,"12th Percentage":lst4,"Branch":lst5},index=[0])
        print(ndf)

        if cho==5:
        x=(input("Enter the Branch : "))
        quer=("select name from college_admission where branch='%d';" %x)
        cur.execute(quer)
        row=cur.fetchall()
        lst=[]
        for z in row:
            for y in z:
                lst.append(y)
        quer1=("select dob from college_admission where branch='%d';" %x) 
        cur.execute(quer1)
        row1=cur.fetchall()
        lst1=[]
        for z in row1:
            for y in z:
                lst1.append(y)
        quer2=("select gender from college_admission where branch='%d';" %x)
        cur.execute(quer2)
        row2=cur.fetchall()
        lst2=[]
        for z in row2:
            for y in z:
                lst2.append(y)
        quer3=("select year_of_admission from college_admission where branch='%d';" %x)
        cur.execute(quer3)
        row3=cur.fetchall()
        lst3=[]
        for z in row3:
            for y in z:
                lst3.append(y)
        quer4=("select 12th_Board_percentage from college_admission where branch='%d';" %x)
        cur.execute(quer4)
        row4=cur.fetchall()
        lst4=[]
        for z in row4:
            for y in z:
                lst4.append(y)
        
        quer5=("select branch from college_admission where branch='%d';" %x)
        cur.execute(quer5)
        row5=cur.fetchall()
        lst5=[]
        for z in row5:
            for y in z:
                lst5.append(y)
        ndf=pd.DataFrame({"Name":lst,"DOB":lst1,"Gender":lst2,"Year of admission":lst3,"12th Percentage":lst4,"Branch":lst5},index=[0])
        print(ndf)


    
