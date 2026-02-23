def factorial(a):
    f=1
    while a>1:
        f=f*a
        a=a-1
    print("Factorial=",f)


factorial(5)
n=int(input("Enter the No"))
factorial(n)
