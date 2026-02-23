import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="vijay")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")
cur=con.cursor()
cur.execute("Select * from Marks")
data=cur.fetchall()
for i in data:
    print(i)
print("_______________________________________________________________")




cur=con.cursor()
cur.execute("Select * from Marks")
data=cur.fetchall()
for i in data:
    print(i[0],i[1],sep="\t")
