def lcm():
    x=int(input("Enter the First Number-"))
    y=int(input("Enter the Second Number-"))
    if x>y:
        a=x
    else:
        a=y
    s=a  # s for storing the value
    while True:
        if  a%x==0 and a%y==0:
            print("The LCM of Number",x,"and",y,"is",a)
            break
        else:
            a=a+s

lcm()
