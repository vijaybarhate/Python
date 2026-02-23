f=open("LICENSE_.txt","r")
g=f.readlines()
f1=open("LICENSEE.txt","w")
l=[]
for i in g:
    if "a" in i:
        f1.write(i)
    else:
        l.append(i)
f2=open("LICENSE_.txt","w")
f2.writelines(l)
f.close()
f2.close()
f1.close()
print("All the lines containing character a have been moved to Another File.")
        
