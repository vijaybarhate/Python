import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="vijay")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")

def mini():
    l=[]
    r=input("Enter the Attribute Name -")
    query="select min({}) from students".format(r)
    cur=con.cursor()
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        l.append([i[0]])
    print(tabulate(l,headers=[r],tablefmt="outline"))

def maxi():
    l=[]
    r=input("Enter the Attribute Name -")
    query="select max({}) from students".format(r)
    cur=con.cursor()
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        l.append([i[0]])
    print(tabulate(l,headers=[r],tablefmt="outline"))

def summ():
    l=[]
    r=input("Enter the Attribute Name -")
    query="select sum({}) from students".format(r)
    cur=con.cursor()
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        l.append([i[0]])
    print(tabulate(l,headers=[r],tablefmt="outline"))

def count():
    l=[]
    r=input("Enter the Attribute Name -")
    query="select {},count(*) from students group by {}".format(r,r)
    cur=con.cursor()
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        l.append([i[0],i[1]])
    print(tabulate(l,headers=[r,r],tablefmt="outline"))

def average():
    l=[]
    r=input("Enter the Attribute Name -")
    query="select avg({}) from students".format(r)
    cur=con.cursor()
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        l.append([i[0]])
    print(tabulate(l,headers=[r],tablefmt="outline"))

choice=0
while choice!=6:
    print("____________________________Enter the Choice_______________________________")
    print("1. To find minmum.")
    print("2. To find maximum")
    print("3. To find sum")
    print("4. To find count")
    print("5. To find average")
    print("6. Exit")
    choice=int(input("Enter your choice -"))
    if choice==1:
        mini()
    elif choice==2:
        maxi()
    elif choice==3:
        summ()
    elif choice==4:
        count()
    elif choice==5:
        average()
    elif choice==6:
        exit
    else:
        print("Invalid Choice")
        break
        
        
