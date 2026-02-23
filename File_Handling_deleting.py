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
DeleteLess()
