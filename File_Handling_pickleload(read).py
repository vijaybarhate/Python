import pickle
d={}
f=open("Students_1.dat","rb")
try:
    while True:
        d=pickle.load(f)
        print(d)
except EOFError:
    f.close()
