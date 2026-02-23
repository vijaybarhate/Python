import os
import pickle
r=int(input("Enter the roll no for which you have to update the record -"))
f=open("Students.dat","rb")
f1=open("Temp.dat","wb")
d={}
try:
    while True:
        d=pickle.load(f)
        if  d["Roll No"]==r:
            print("Plz enter new marks for roll no -",r)
            m=float(input("Enter the new Marks obtained by the student -"))
            d["Marks"]=m
            pickle.dump(d,f1)
        else:
            pickle.dump(d,f1)
except EOFError:
    f.close()
    f1.close()
    os.remove("Students_1.dat")
    os.rename("Temp.dat","Students_1.dat")
    print("Record Updated Successfully")
        
