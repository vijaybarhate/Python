import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="vijay")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")
    
def add_new_attribute():
    a=input("Enter the Name of the Atrribute -")
    b=input("Enter the datatype of the Attribute -")
    c=int(input("Enter the display length of the Attribute -"))
    query="ALTER TABLE Students ADD {} {}({})".format(a,b,c)
    cur=con.cursor()
    cur.execute(query)
    con.commit()

def modify_data_type():
    a=input("Enter the Name of the Atrribute to be modified -")
    b=input("Enter the datatype of the Attribute -")
    c=int(input("Enter the display length of the Attribute -"))
    query=" ALTER TABLE students Modify column {} {}({})".format(a,b,c)
    cur=con.cursor()
    cur.execute(query)
    con.commit()

def drop_attribute():
    a=input("Enter the Name of the Atrribute to be deleted or droped from table -")
    query="ALTER TABLE students DROP {}".format(a)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    
choice=0
while choice!=4:
    print("____________________________Enter the Choice_______________________________")
    print("1. To Add new Attribute")
    print("2. To Modify data type")
    print("3. To Drop Attribute")
    print("4. Exit")
    choice=int(input("Enter your choice -"))
    if choice==1:
        add_new_attribute()
    elif choice==2:
        modify_data_type()
    elif choice==3:
        drop_attribute()
    elif choice==4:
        exit
    else:
        print("Invalid Choice")
        break
        
        
        
