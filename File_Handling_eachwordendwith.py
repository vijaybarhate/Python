f=open("LICENSE_.txt","r")
m=f.readlines()
for i in m:
    i=i.split()
    for j in i:
        print(j,end="#")

