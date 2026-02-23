# defining a function to calculate HCF  
def hcf(): 
    x = int(input("Enter first number: "))  
    y = int(input("Enter second number: ")) 
    # selecting the smaller number  
    if x > y:  
        smaller = y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return hcf  
  
# taking input from users  
  
# printing the result for the users  
print(hcf())  
