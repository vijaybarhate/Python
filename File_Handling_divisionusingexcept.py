a=int(input("Enter the First Number -"))
b=int(input("Enter the Second Number -"))
c=0
try:
    c=a/b
    print("Answer will be - ",c)
except ZeroDivisionError:
    print("Answer will be - Infinite")
