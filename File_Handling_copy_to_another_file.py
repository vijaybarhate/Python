import os
import pickle
f=open("Students.dat","rb")
f1=open("Temp.dat","wb")
d={}
try:
    while True:
        d=pickle.load(f)
        pickle.dump(d,f1)
except EOFError:
    f.close()
    f1.close()
    c=input("Enter the New Name for the File:")
    os.remove("Students_1.dat")
    os.rename("Temp.dat",c)
    print("Record Updated Successfully")
        
