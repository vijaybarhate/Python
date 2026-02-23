f=open("LICENSE_1.txt","r")
s=f.read()
a=0
d=0
b=0
for i in s:
    if i.isalpha():
        a=a+1
    elif i.isdigit():
        d=d+1
    else:
        b=b+1
print("The number of Alphabets present in the file are -",a)
print("The number of Digits present in the file are -",d)
print("The number of Special Characters present in the file are -",b)
