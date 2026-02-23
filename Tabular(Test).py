from tabulate import tabulate
data=(["Swift"], ["Java"], ["Python"])
print(tabulate(data, tablefmt="outline"))


print("____________________________Enter the Choice_______________________________")
print("1. Search with Roll No :")
print("2. Search with Name :")
print("3. Search with Admission No :")
print("4. Search with Class :")
print("5. Search with Address :")
print("6. See all Record :")
print("7. Exit")

a=(["1. Search with Roll No :"],["2. Search with Name :"],["3. Search with Admission No :"],["4. Search with Class :"],["5. Search with Address :"],["6. See all Record :"],["7. Exit"])
print(tabulate(a,headers=[">>>>>>Enter the Choice<<<<<<"],tablefmt="outline"))
