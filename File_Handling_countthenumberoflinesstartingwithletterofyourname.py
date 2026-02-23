f=open("LICENSE_1.txt","r")
c=0
s=f.readlines()
p=input("Enter a Character(Alphabet) -")
for i in s:
    if i[0]==p:
        c=c+1
    else:
        c=c
print("The number of lines starting with the letter",p,"are=",c)
