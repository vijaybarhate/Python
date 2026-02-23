import csv
f=open("Students_2.csv","r")
d=csv.reader(f,delimiter="|")
for i in d:
    print(i)
f.close()
