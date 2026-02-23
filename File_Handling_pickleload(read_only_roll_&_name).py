import pickle
f=open("Student.dat","rb")
d={}
print("Student Name","Roll Number \n",sep="\t")
try:
    while True:
        d=pickle.load(f)
        print(d["Name"],str(d["Roll No"])+"\n",sep="\t"+"\t"+"  ")
except EOFError:
    f.close()
