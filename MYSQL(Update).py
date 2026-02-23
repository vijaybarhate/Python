import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="vijay")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")

def update():
    oldr=int(input("Enter the Rollno of the students whose name you want to change -"))
    newn=input("Enter the Name to be updated -")
    query="update students set s_name='{}' where roll_no={}".format(newn,oldr)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("Successfully Updated")

update()
