import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="school")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")
cur=con.cursor()
def Deletee():
    n=input("Enter the Name of the student -")
    quer="select Roll_No from student where Name='{}'".format(n)
    cur.execute(quer)
    data=cur.fetchall()
    for i in data:
        a=i[0]
    
Deletee()
