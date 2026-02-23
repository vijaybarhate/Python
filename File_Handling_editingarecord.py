import pickle
fin=open("Students.dat","rb")
fout=open("Distinction.dat","wb")
d={}
found=False
try:
    while True:
        d=pickle.load(fin)
        if d["Marks"]>80:
            pickle.dump(d,fout)
            found=True
            print("Student Name","Roll Number","Marks \n",sep="\t")
            print(d["Name"],str(d["Roll No"]),str(d["Marks"])+"\n",sep="\t"+"\t"+"  ")
except EOFError:
    if found==False:
        print("No Records found as per given Conditiion")
    else:
        print("Mission Successful")
    fin.close()
    fout.close()
