f=open("LICENSE_2.txt","w")
q=int(input("Enter the number of Students:"))
for i in range(1,q+1):
      name=input("Enter the Name of the Student",i,":")
      age=int(input("Enter the age of the Student",i,":"))
      roll_no=int(input("Enter the Roll No. of the Student",i,":"))
      marks=float(input("Enter the Marks scored by the Student",i,":"))
      a=name+","+str(age)+","+str(roll_no)+","+str(marks)+"\n"
      f.write(name+a+r+m)
f.close()
    
