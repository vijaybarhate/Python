import csv
with open("Practical.csv", "r") as obj2:
    fileobj2 = csv.reader(obj2)
    given = input("enter the user id to be searched\n")

    for i in fileobj2:
        next(fileobj2)

        # print(i,given)
        if i[0] == given:
            print(i[1])
            break
obj2.close()
