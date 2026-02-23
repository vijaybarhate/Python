import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="vijay")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")


def insert():
    s_name=input("Enter the Name of the student -")
    roll_no=int(input("Enter the Roll No. of the students -"))
    address=input("Enter the Address of the Student - ")
    marks=float(input("Enter the marks obtained by the student -"))
    query="insert into students values('{}',{},'{}',{})".format(s_name,roll_no,address,marks)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
def update():
    oldr=int(input("Enter the Rollno of the students whose name you want to change -"))
    newn=input("Enter the Name to be updated -")
    query="update students set s_name='{}' where roll_no={}".format(newn,oldr)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
def delete():
    r=int(input("Enter the Rollno of the students of whose record you want to delte -"))
    query="delete from students where roll_no={}".format(r)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    
def display():
    cur=con.cursor()
    cur.execute("Select * from students")
    data=cur.fetchall()
    for i in data:
        print(i)

    



choice=0
while choice!=5:
    print("____________________________Enter the Choice_______________________________")
    print("1. To Insert a record")
    print("2. To Update a record")
    print("3. To Delete a record")
    print("4. To Display a record")
    print("5. Exit")
    choice=int(input("Enter your choice -"))
    if choice==1:
        insert()
    elif choice==2:
        update()
    elif choice==3:
        delete()
    elif choice==4:
        display()
    elif choice==5:
        exit
    else:
        print("Invalid Choice")
        break
        
        
        
