import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="vijay")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")

def ascending_order():
    l=[]
    a=input("Enter the Column or Attribute to be used for ordering the record -")
    query="select * from students order by {}".format(a)
    cur=con.cursor()
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        l.append([i[0],i[1],i[2],i[3]])
    print(tabulate(l,headers=["Name","Roll No","Address","Marks"],tablefmt="outline"))

def descending_order():
    l=[]
    a=input("Enter the Column or Attribute to be used for ordering the record -")
    query="select * from students order by {} desc".format(a)
    cur=con.cursor()
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        l.append([i[0],i[1],i[2],i[3]])
    print(tabulate(l,headers=["Name","Roll No","Address","Marks"],tablefmt="outline"))

choice=0
while choice!=3:
    print("____________________________Enter the Choice_______________________________")
    print("1. To display data in Ascending Order")
    print("2. To display data in Descending Order")
    print("3. Exit")
    choice=int(input("Enter your choice -"))
    if choice==1:
        ascending_order()
    elif choice==2:
        descending_order()
    elif choice==3:
        exit
    else:
        print("Invalid Choice")
        break
