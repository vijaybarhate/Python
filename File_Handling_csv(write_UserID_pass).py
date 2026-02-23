import csv
f=open("Practical.csv","w",newline='')
d=csv.writer(f)
d.writerow(["User ID","Password"])
ans='y'
while ans=='y':
    user=input("Enter User ID:")
    pas=input("Enter Password:")
    a=[user,pas]
    d.writerow(a)
    print("Successfully added a new Record")
    ans=input("Do you want to add more Records? press 'y' for adding more records ......=")
f.close()
