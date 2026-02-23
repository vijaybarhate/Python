import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="school")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")
cur=con.cursor()
def Viewwwwww():
    l=[]
    cur.execute("Select * from student")
    data=cur.fetchall()
    for i in data:
        l.append([i[0],i[1],i[2],i[3],i[4]])
    print(tabulate(l,headers=["Roll No","Name","Admission No","Clas","Address"],tablefmt="outline"))


Viewwwwww()
