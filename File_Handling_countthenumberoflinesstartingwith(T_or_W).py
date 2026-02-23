f=open("LICENSE_.txt","r")
c=0
p=["t","T","w","W"]
s=f.readlines()
for i in s:
    if i[0] in p:
        c=c+1
    else:
        c=c
print("The number of lines starting with the letter",p,"are=",c)
