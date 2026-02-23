import csv
r=input("Enter the roll no to be searched in the record -")
f=open("Students_2.csv","r")
d=csv.reader(f)
for i in d:
    if i[0]==r:
        print("searching for Roll Number -",r," in the Record")
        a=i[0]
        b=i[1]
        c=i[2]
print("Rollno","Name","Marks",sep='\t')
print(a,b,c,sep='\t')
f.close()
print("Record found Successfully")
        
