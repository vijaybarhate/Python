def addition():
    a=int(input("Enter the First Number-"))
    b=int(input("Enter the Second Number-"))
    return a+b
def substract():
    a=int(input("Enter the Greater Number-"))
    b=int(input("Enter the Second Number-"))
    return a-b
def multiply():
    a=int(input("Enter the First Number-"))
    b=int(input("Enter the Second Number-"))
    return a*b
def divide():
    a=int(input("Enter the Greater Number-"))
    b=int(input("Enter the Second Number-"))
    return a//b

choice=0
while choice!=5:
    print("1. For ADDITION of two numbers")
    print("2. For SUBSTRACTION of two numbers")
    print("3. For MULTIPLICATION of two numbers")
    print("4. For DIVISION of two numbers")
    print("5. Exit")
    print("____________________________________________")
    choice=int(input("Enter Your Choice between 1 to 5 -"))
    if choice==1:
        c=addition()
        print("Answer is",c)
    elif choice==2:
        c=substract()
        print("Answer is",c)
    elif choice==3:
        c=multiply()
        print("Answer is",c)
    elif choice==4:
        c=divide()
        print("Answer is",c)
    elif choice==5:
        exit
    else:
        print("Invalid Choice")

