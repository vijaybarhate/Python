import os
import pickle
fin=open("Students.dat","rb")
fout=open("Temp.dat","wb")
d={}
found=False
roll=int(input("Enter the Roll No:"))
print("The Record of Roll No ",roll," will be deleted")
print("Student Name","Roll Number","Marks \n",sep="\t")
try:
    while True:
        d=pickle.load(fin)
        if d["Roll No"]!=roll:
            pickle.dump(d,fout)
            found=True
            print(d["Name"],str(d["Roll No"]),str(d["Marks"])+"\n",sep="\t"+"\t"+"  ")
except EOFError:
    if found==False:
        print("No Record was found with Conditions applied")
        fin.close()
        fout.close()
    else:
        fin.close()
        fout.close()
        os.remove("Students_1.dat")
        os.rename("Temp.dat","Students_1.dat")
        print("Mission Successful")
