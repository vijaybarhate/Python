import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="school")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")
cur=con.cursor()
def View():
    r=int(input("Enter the Rollno of the student -"))
    d={}
    found=0
    query="select * from student where Roll_No={}".format(r)
    cur.execute(query)
    data=cur.fetchall()
    for i in data:
        if i[0]==r:
            found=1
            a=i[0]
            b=i[1]
            c=i[2]
            de=i[3]
            e=i[4]
            d["Roll No"]=str(a)
            d["Name"]=b
            d["Admission No"]=c
            d["Class"]=str(de)
            d["Address"]=e
            print('''


''')
            print(tabulate([[d["Roll No"],d["Name"],d["Admission No"],d["Class"],d["Address"]]],headers=["Roll No","Name","Admission No","Clas","Address"],tablefmt="outline"))
            print('''


''')
    if found==1:
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

Viewwwwww()
