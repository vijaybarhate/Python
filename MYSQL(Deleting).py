import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="vijay")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")

def delete():
    a=int(input("Enter the Roll number of the student -"))
    query="DELETE FROM students WHERE roll_no={}".format(a)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("Deleted Successfully.")

delete()
