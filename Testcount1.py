def counter():
    f=open("Testcount1.txt","r")
    m=f.read()
    s=m.split()
    a=0
    p=input("Enter the word whose Occurance you need to count -")
    for i in s:
        if i==p:
            a=a+1
        else:
            a=a
    print("The Occurance of the word",p,"is done",a,"number of times in the file.")
        
def counter1():
    f=open("Testcount1.txt","r")
    m=f.read()
    a=0
    p=input("Enter the word whose Occurance you need to count -")
    for i in m:
        if i==p:
            a=a+1
        else:
            a=a
    print("The Occurance of the word",p,"is done",a,"number of times in the file.")


counter1()
