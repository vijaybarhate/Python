import os
import csv
r=input("Enter the roll no for which you have to update the record -")
f=open("Students_2.csv","r")
f1=open("Temp.csv","w",newline='\n')
d=csv.reader(f)
wt=csv.writer(f1)
for i in d:
    if i[0]==r:
        print("Plz enter new marks for roll no -",r)
        m=float(input("Enter the new Marks obtained by the student -"))
        i[2]=m
    wt.writerow(i)
f.close()
f1.close()
os.remove("Students_2.csv")
os.rename("Temp.csv","Students_2.csv")
print("Record Updated Successfully")
        
