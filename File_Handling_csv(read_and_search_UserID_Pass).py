import csv
f=open("Practical.csv","r")
d=csv.reader(f)
w=input("Enter UserID:")
for i in d:
    if i[0]==w:
        print(i[1])
f.close()
