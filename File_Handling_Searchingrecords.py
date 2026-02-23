import pickle
f=open("Students.dat","rb")
d={}
print("*********************__Searching_with_Roll_No__**********************")
w=int(input("Enter the ROLL NUMBER of the Student you want to search record of -"))
wf=False
try:
        print("Searching Records . ............. . .")
        while True:
                    d=pickle.load(f)
                    if d["Roll No"]==w:
                        wf=True
                        print("Student Name","Roll Number","Marks \n",sep="\t")
                        print(d["Name"],str(d["Roll No"]),str(d["Marks"])+"\n",sep="\t"+"\t"+"  ")
except EOFError:
                if wf==False:
                    print("No Record was found")
                else:
                    print("Record found Successfully☝")
                f.close()
