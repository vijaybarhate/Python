import csv
f=open("Students_2.csv","w",newline='')
d=csv.writer(f)
d.writerow(["Roll No","Name","Marks"])
ans='y'
while ans=='y':
    rno=int(input("Enter the Roll number of the Student:"))
    name=input("Enter the name of the Student:")
    marks=float(input("Enter the Marks obtained by Student:"))
    a=[rno,name,marks]
    d.writerow(a)
    print("Successfully added a new Record")
    ans=input("Do you want to add more Records? press 'y' for adding more records ......=")
f.close()
