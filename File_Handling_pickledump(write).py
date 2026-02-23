import pickle
d={}
f=open("Students.dat","ab")
ans='y'
while ans=='y':
    rno=int(input("Enter the Roll number of the Student:"))
    name=input("Enter the name of the Student:")
    marks=float(input("Enter the Marks obtained by Student:"))
    d["Roll No"]=rno
    d["Name"]=name
    d["Marks"]=marks
    pickle.dump(d,f)
    print("Successfully added a new Record")
    ans=input("Do you want to add more Records? press 'y' for adding more records ......=")
f.close()
