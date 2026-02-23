import pickle
f=open("newstudent.dat","rb")
d={}
print("Student Name","Roll Number","Marks \n",sep="\t")
try:
    while True:
        d=pickle.load(f)
        print(d["Name"],str(d["Roll No"]),str(d["Marks"])+"\n",sep="\t"+"\t"+"  ")
except EOFError:
    f.close()
