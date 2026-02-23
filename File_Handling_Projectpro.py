def Search():
    import pickle
    f=open("Students_1.dat","rb")
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
                    return "No Record was found"
                else:
                    return "Record found Successfully☝"
                f.close()
def SearchName():
    import pickle
    f=open("Students_1.dat","rb")
    d={}
    print("*********************__Searching_with_Roll_No__**********************")
    w=input("Enter the NAME of the Student you want to search record of -")
    wf=False
    try:
            print("Searching Records . ............. . .")
            while True:
                    d=pickle.load(f)
                    if d["Name"]==w:
                        wf=True
                        print("Student Name","Roll Number","Marks \n",sep="\t")
                        print(d["Name"],str(d["Roll No"]),str(d["Marks"])+"\n",sep="\t"+"\t"+"  ")
    except EOFError:
                if wf==False:
                    return "No Record was found"
                else:
                    return "Record found Successfully☝"
                f.close()
def Add():
    import pickle
    d={}
    f=open("Students_1.dat","ab")
    ans='y'
    while ans=='y':
        rno=int(input("Enter the Roll number of the Student:"))
        name=input("Enter the name of the Student:")
        marks=float(input("Enter the Marks obtained by Student:"))
        d["Roll No"]=rno
        d["Name"]=name
        d["Marks"]=marks
        pickle.dump(d,f)
        print("Successfully added a new Record")
        ans=input("Do you want to add more Records? press 'y' for adding more records ......=")
    f.close()

def Edit():
    import os
    import pickle
    r=int(input("Enter the roll no for which you have to update the record -"))
    f=open("Students_1.dat","rb")
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
        
def DeleteLess():
    import os
    import pickle
    with open("Students_1.dat", "rb") as fin:
        d={}
        print("Enter the Folowing")
        v=int(input("Enter the Marks -"))
        print("Records containg Marks more than ",v,"will be deleted")
        found=False
        try:
            while True:
                d=pickle.load(fin)
                if d["Marks"]<v:
                    with open("Temp.dat", "wb") as fout:
                        pickle.dump(d,fout)
                        found=True
        except EOFError:
            if found==False:
                return "No Record was found with Conditions applied"
            fin.close()
            fout.close()
            os.remove("Students_1.dat")
            os.rename("Temp.dat","Students_1.dat")

def DeleteEqual():
    import os
    import pickle
    fin=open("Students_1.dat","rb")
    fout=open("Temp.dat","wb")
    d={}
    print("Enter the Folowing")
    v=int(input("Enter the Marks -"))
    print("Records containg Marks more than ",v,"will be deleted")
    found=False
    try:
        while True:
            d=pickle.load(fin)
            if d["Marks"]!=v:
                pickle.dump(d,fout)
                found=True
    except EOFError:
        fin.close()
        fout.close()
        os.remove("Students_1.dat")
        os.rename("Temp.dat","Students_1.dat")
        if found==False:
            return "No Record was found with Conditions applied"
        
def DeleteRoll():
    import os
    import pickle
    fin=open("Students_1.dat","rb")
    fout=open("Temp.dat","wb")
    d={}
    print("Enter the Folowing")
    v=int(input("Enter the Roll Number -"))
    print("Records containg Roll No- ",v,"will be deleted")
    found=False
    try:
        while True:
            d=pickle.load(fin)
            if d["Roll No"]!=v:
                pickle.dump(d,fout)
                found=True
    except EOFError:
        fin.close()
        fout.close()
        os.remove("Students_1.dat")
        os.rename("Temp.dat","Students_1.dat")
        if found==False:
            return "No Record was found with Conditions applied"
        
def DeleteMore():
    import os
    import pickle
    fin=open("Students_1.dat","rb")
    fout=open("Temp.dat","wb")
    d={}
    print("Enter the Folowing")
    v=int(input("Enter the Marks -"))
    print("Records containg Marks less than ",v,"will be deleted")
    found=False
    try:
        while True:
            d=pickle.load(fin)
            if d["Marks"]>v:
                pickle.dump(d,fout)
                found=True
    except EOFError:
        if found==False:
            return "No Record was found with Conditions applied"
        fin.close()
        fout.close()
        os.remove("Students_1.dat")
        os.rename("Temp.dat","Students_1.dat")
def Read():
    import pickle
    f=open("Students_1.dat","rb")
    d={}
    print("Student Name","Roll Number","Marks \n",sep="\t")
    try:
        while True:
            d=pickle.load(f)
            print(d["Name"],str(d["Roll No"]),str(d["Marks"])+"\n",sep="\t"+"\t"+"  ")
    except EOFError:
        f.close()
def Loop1():
    choice=0
    m=0
    a=0
    b=0
    while a!=3:
            print("1. Search with Name ")
            print("2. Search with Roll No")
            print("3. Exit")
            a=int(input("Enter the Choice from 1 to 3 --"))
            if a==1:
                l=SearchName()
                print(l)
            elif a==2:
                l=Search()
                print(l)
            elif a==3:
                print("Program Closed")
                exit
            else:
                print("Invalid Choice")
                break
def Loop2():
    choice=0
    m=0
    a=0
    b=0
    while m!=5:
            print("1. Delete Record for marks less than")
            print("2. Delete Record for marks more than")
            print("3. Delete Record for marks Equal To ")
            print("4. Delete Record for Roll No equal to")
            print("5. Exit")
            m=int(input("Enter your Choice from 1 to 5 -"))
            if m==1:
                l=DeleteMore()
                print(l)
            elif m==2:
                l=DeleteLess()
                print(l)
            elif m==3:
                l=DeleteEqual()
                print(l)
            elif m==4:
                l=DeleteRoll()
                print(l)
            elif m==5:
                print("Program Closed")
                exit
            else:
                print("Invalid Choice")
                break

choice=0
m=0
a=0
b=0
while choice!=6:
    print("******************__FILE_HANDLING__*******************")
    print("1. To Add Records in File.")
    print("2. To perform Search in the Record.")
    print("3. To Edit or Update Record in File.")
    print("4. To Delete Record in File.")
    print("5. To Show or Read Record from File.")
    print("6. To Exit.")
    choice=int(input("Enter your Choice from 1 to 6 -"))
    if choice==1:
        l=Add()
        print(l)
    elif choice==2:
        Loop1()
    elif choice==3:
        l=Edit()
        print(l)
    elif choice==4:
        Loop2()
    elif choice==5:
        l=Read()
        print(l)
    elif choice==6:
        print("Program Closed")
        exit
    else:
        print("Invalid Choice")
        break
            
        

