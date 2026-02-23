import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="Students_fee_management_system")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")
cur=con.cursor()
r=int(input("Enter the Rollno of the student -"))
query="select * from student where Roll_No={}".format(r)
cur.execute(query)
data=cur.fetchall()
print("Roll No","        Name","        Admission No","Class","        Address",sep="\t")
for i in data:
    print(i[0],i[1],i[2],i[3],i[4],sep="\t\t")
