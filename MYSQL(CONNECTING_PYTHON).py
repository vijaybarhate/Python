import mysql.connector
a=input("Enter the Password-")
con=mysql.connector.connect(host="localhost",user="root",passwd=a,database="ConnectPython")
if con.is_connected():
    print("Successfully connected to the Database.")
else:
    print("No Database found.")
