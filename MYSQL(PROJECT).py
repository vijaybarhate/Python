import mysql.connector
from tabulate import tabulate
import pyfiglet
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="school")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")
cur=con.cursor()


def Add():
    n=input("Enter the Name of the student -")
    r=int(input("Enter the Roll No. of the student -"))
    a=input("Enter the Address of the Student - ")
    clas=input("Enter the Class the student -")
    ad=int(input("Enter the Admission No. of the students -"))
    query="insert into student values({},'{}',{},'{}','{}')".format(r,n,ad,clas,a)
    cur.execute(query)
    con.commit()
    print("Added Succesfully")


def Delete():
    r=int(input("Enter the Rollno of the student of whose record you want to delete -"))
    query="delete from student where Roll_no={}".format(r)
    cur.execute(query)
    q="delete from fees where Roll_no={}".format(r)
    cur.execute(q)
    con.commit()
    print("Record Deleted")

def Deletee():
    n=input("Enter the Name of the student -")
    quer="select Roll_No from student where Name='{}'".format(n)
    cur.execute(quer)
    data=cur.fetchall()
    for i in data:
        a=i[0]
    q="delete from fees where Roll_no={}".format(a)
    cur.execute(q)
    con.commit()
    print("Record Deleted")

def Deleteee():
    ad=int(input("Enter the Admission No. of the students -"))
    quer="select Roll_No from student where Admission_No='{}'".format(ad)
    cur.execute(quer)
    data=cur.fetchall()
    for i in data:
        a=i[0]
    q="delete from fees where Roll_no={}".format(a)
    cur.execute(q)
    con.commit()
    print("Record Deleted")


def Deleteeee():
    clas=input("Enter the Class the student -")
    quer="select Roll_No from student where Class='{}'".format(clas)
    cur.execute(quer)
    data=cur.fetchall()
    for i in data:
        a=i[0]
    q="delete from fees where Roll_no={}".format(a)
    cur.execute(q)
    con.commit()
    print("Record Deleted")

def Deleteeeee():
    a=input("Enter the Address of the Student - ")
    quer="select Roll_No from student where Address='{}'".format(a)
    cur.execute(quer)
    data=cur.fetchall()
    for i in data:
        a=i[0]
    q="delete from fees where Roll_no={}".format(a)
    cur.execute(q)
    con.commit()
    print("Record Deleted")

def Deleteeeeee():
    quer="delete from student"
    cur.execute(quer)
    q="delete from fees"
    cur.execute(q)
    con.commit()
    print("Records Deleted")
    

def View():
    r=int(input("Enter the Rollno of the student -"))
    l=[]
    found=0
    query="select * from student where Roll_No={}".format(r)
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        if i[0]==r:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4]])

    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Admission No","Clas","Address"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    
        
def Vieww():
    n=input("Enter the Name of the student -")
    l=[]
    q="select * from student where Name='{}'".format(n)
    cur.execute(q)
    data=cur.fetchall()
    found=0
    for i in data:
        if i[1]==n:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4]])
    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Admission No","Clas","Address"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    
        
def Viewww():
    l=[]
    ad=int(input("Enter the Admission No. of the students -"))
    q="select * from student where Admission_No={}".format(ad)
    cur.execute(q)
    data=cur.fetchall()
    found=0
    for i in data:
        if i[2]==ad:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4]])
    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Admission No","Clas","Address"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    
    
def Viewwww():
    l=[]
    clas=input("Enter the Class the student -")
    q="select * from student where Class='{}'".format(clas)
    cur.execute(q)
    data=cur.fetchall()
    found=0
    for i in data:
        if i[3]==clas:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4]])
    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Admission No","Clas","Address"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    

    
def Viewwwww():
    l=[]
    a=input("Enter the Address of the Student - ")
    q="select * from student where Address='{}'".format(a)
    cur.execute(q)
    data=cur.fetchall()
    found=0
    for i in data:
        if i[4]==a:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4]])
    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Admission No","Clas","Address"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    

    
def Viewwwwww():
    l=[]
    cur.execute("Select * from student")
    data=cur.fetchall()
    for i in data:
        l.append([i[0],i[1],i[2],i[3],i[4]])
    print(tabulate(l,headers=["Roll No","Name","Admission No","Clas","Address"],tablefmt="outline"))    


        
def Deposit():
    r=int(input("Enter the Rollno of the student -"))
    f=10000
    i=int(input("Enter the Month of Fee(In Numbers i.e, 1 for Jan like that) - "))
    if i==1:
        m="January"
    elif i==2:
        m="Februaury"
    elif i==3:
        m="March"
    elif i==4:
        m="April"
    elif i==5:
        m="May"
    elif i==6:
        m="June"
    elif i==7:
        m="July"
    elif i==8:
        m="August"
    elif i==9:
        m="September"
    elif i==10:
        m="October"
    elif i==11:
        m="November"
    elif i==12:
        m="December"
    else:
        print("Incorrect Detail")
    a=(["1. UPI"],["2. Cash"],["3. Credit/Debit Card"])
    print(tabulate(a,headers=[">>>>>>Select the Payment Mode<<<<<<"],tablefmt="rounded_outline"))
    o=int(input("Enter the Payment Mode:"))
    if o==1:
        p="UPI"
    elif o==2:
        p="Cash"
    elif o==3:
        p='''Debit Card'''
    else:
        p="Unknown"    
    query="insert into fees values({},{},'{}','{}')".format(r,f,m,p)
    cur.execute(query)
    con.commit()


def View2():
    r=int(input("Enter the Rollno of the student -"))
    l=[]
    query="select s.Roll_No,s.Name,s.Class,s.Address,s.Admission_No,f.Fee_Deposit,f.month,f.Payment_mode from student s,fees f where s.Roll_No=f.Roll_No and s.Roll_No={}".format(r)
    cur.execute(query)
    data=cur.fetchall()
    found=0
    for i in data:
        if i[0]==r:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Class","Address","Admission No","Fees Deposit","Month","Payment Mode"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    

        
def View22():
    n=input("Enter the Name of the student -")
    l=[]
    query="select s.Roll_No,s.Name,s.class,s.Address,s.Admission_No,f.Fee_Deposit,f.month,f.Payment_mode from student s,fees f where s.Roll_No=f.Roll_No and s.Name='{}'".format(n)
    cur.execute(query)
    data=cur.fetchall()
    found=0
    for i in data:
        if i[1]==n:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Class","Address","Admission No","Fees Deposit","Month","Payment Mode"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    


def View222():
    l=[]
    ad=int(input("Enter the Admission No. of the students -"))
    query="select s.Roll_No,s.Name,s.class,s.Address,s.Admission_No,f.Fee_Deposit,f.month,f.Payment_mode from student s,fees f where s.Roll_No=f.Roll_No and s.Admission_No={}".format(ad)
    cur.execute(query)
    data=cur.fetchall()
    found=0
    for i in data:
        if i[4]==ad:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Class","Address","Admission No","Fees Deposit","Month","Payment Mode"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    

def View2222():
    l=[]
    clas=input("Enter the Class the student -")
    query="select s.Roll_No,s.Name,s.class,s.Address,s.Admission_No,f.Fee_Deposit,f.month,f.Payment_mode from student s,fees f where s.Roll_No=f.Roll_No and s.Class={}".format(clas)
    cur.execute(query)
    data=cur.fetchall()
    found=0
    for i in data:
        if i[2]==clas:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Class","Address","Admission No","Fees Deposit","Month","Payment Mode"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    


def View22222():
    l=[]
    a=input("Enter the Address of the Student - ")
    query="select s.Roll_No,s.Name,s.class,s.Address,s.Admission_No,f.Fee_Deposit,f.month,f.Payment_mode from student s,fees f where s.Roll_No=f.Roll_No and s.Address={}".format(a)
    cur.execute(query)
    data=cur.fetchall()
    found=0
    for i in data:
        if i[3]==a:
            found=1
            l.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    if found==1:
        print('''


''')
        print(tabulate(l,headers=["Roll No","Name","Class","Address","Admission No","Fees Deposit","Month","Payment Mode"],tablefmt="outline"))
        print('''


''')
        print("Record was found Succesfully1")
    else:
        print("Record not Found")
    



def View222222():
    l=[]
    query="select s.Roll_No,s.Name,s.class,s.Address,s.Admission_No,f.Fee_Deposit,f.month,f.Payment_mode from student s,fees f where s.Roll_No=f.Roll_No"
    cur.execute(query)
    data=cur.fetchall()
    found=0
    for i in data:
        l.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    print(tabulate(l,headers=["Roll No","Name","Class","Address","Admission No","Fees Deposit","Month","Payment Mode"],tablefmt="outline"))









def menu():
    z=0
    while z!=7:
        a=(["1. Search with Roll No :"],["2. Search with Name :"],["3. Search with Admission No :"],["4. Search with Class :"],["5. Search with Address :"],["6. See all Record :"],["7. Exit"])
        print(tabulate(a,headers=[">>>>>>Enter the Choice<<<<<<"],tablefmt="rounded_outline"))
        z=int(input("Enter your choice -"))
        if z==1:
            View()
        elif z==2:
            Vieww()
        elif z==3:
            Viewww()
        elif z==4:
            Viewwww()
        elif z==5:
            Viewwwww()
        elif z==6:
            Viewwwwww()
        elif z==7:
            print("Program Closed")
            exit
        else:
            print("Invalid Choice")
            break

def menu2():
    z=0
    while z!=7:
        a=(["1. Search with Roll No :"],["2. Search with Name :"],["3. Search with Admission No :"],["4. Search with Class :"],["5. Search with Address :"],["6. See all Record :"],["7. Exit"])
        print(tabulate(a,headers=[">>>>>>Enter the Choice<<<<<<"],tablefmt="rounded_outline"))
        z=int(input("Enter your choice -"))
        if z==1:
            View2()
        elif z==2:
            View22()
        elif z==3:
            View222()
        elif z==4:
            View2222()
        elif z==5:
            View22222()
        elif z==6:
            View222222()
        elif z==7:
            print("Program Closed")
            exit
        else:
            print("Invalid Choice")
            break

def menu3():
    x=0
    while x!=7:
        a=(["1. Search with Roll No :"],["2. Search with Name :"],["3. Search with Admission No :"],["4. Search with Class :"],["5. Search with Address :"],["6. Delete all Record :"],["7. Exit"])
        print(tabulate(a,headers=[">>>>>>Enter the Choice<<<<<<"],tablefmt="rounded_outline"))
        x=int(input("Enter your choice -"))
        if x==1:
            Delete()
        elif x==2:
            Deletee()
        elif x==3:
            Deleteee()
        elif x==4:
            Deleteeee()
        elif x==5:
            Deleteeeee()
        elif x==6:
            Deleteeeeee()
        elif x==7:
            print("Program Closed")
            exit
        else:
            print("Invalid Choice")
            break











def mainmenu():
    choice=0
    while choice!=6:
        print("\n\n")
        print(pyfiglet.figlet_format("Welcome",font="starwars",width=150,justify="center"))
        print(pyfiglet.figlet_format("TO",font="starwars",width=150,justify="center"))
        print(pyfiglet.figlet_format("A V N School",font="starwars",width=150,justify="center"))
        print(pyfiglet.figlet_format("fee",font="starwars",width=150,justify="center"))
        print(pyfiglet.figlet_format("Management",font="starwars",width=150,justify="center"))
        print(pyfiglet.figlet_format("system",font="starwars",width=150,justify="center"))
        
        a=(["1. To Add a Student"],["2. To Delete a Student"],["3. To View student detail"],["4. To Deposit Fee"],["5. To View Fee of a Student"],["6. Exit"])
        print(tabulate(a,headers=[">>>>>>Enter the Choice<<<<<<"],tablefmt="rounded_outline"))
        choice=int(input("Enter your choice -"))
        if choice==1:
            Add()
        elif choice==2:
            menu3()
        elif choice==3:
            menu()
        elif choice==4:
            Deposit()
        elif choice==5:
            menu2()
        elif choice==6:
            print(pyfiglet.figlet_format("T h a n k s",font="isometric1",width=150,justify="center"))
            print("\t\t\t\t\t\t\t\t\t\t\t\t   Thank for using the Program.(Designed by - Mr.Vijay Barhate)")
            exit
        else:
            print("Invalid Choice")
            break


mainmenu()
