f=open("LICENSE_.txt","r")
s=f.read()
l=0
u=0
v=0
c=0
for i in s:
    if i.islower():
        l=l+1
    elif i.isupper():
        u=u+1
    i=i.lower()
    if i in ['a','e','i','o','u']:
        v=v+1
    elif i in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
        c=c+1
        
        
print("The number of Lowercase Characters present in the file are -",l)
print("The number of Uppercase Characters present in the file are -",u)
print("The number of Vowels present in the file are -",v)
print("The number of Consonants present in the file are-",c)
f.close()
