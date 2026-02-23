def Push(stk,x):                
    stk.append(x)
    top=len(stk)-1

    
def Pop(stk):
    if stk==[]:
        return "UNDERFLOW!"
    else:
        t=stk.pop()
        top=len(stk)-1
        print("Removed Value or Item from the list -",t)

        
def Display(stk):
    if stk==[]:
        print("UNDERFLOW! Stack is Empty")
    else:
        top=len(stk)-1
        print("Displayinig the Data-")
        for i in range(top,-1,-1):
            print(stk[i])


SList=[]
choice=0
while choice!=4:
    print("********************__STACK_OPERATIONS__************************")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice=int(input("Enter your choice(1 to 4):-"))
    if choice==1:
        x=int(input("Enter the Value to Push:-"))
        Push(SList,x)
    elif choice==2:
        Pop(SList)
    elif choice==3:
        Display(SList)
    elif choice==4:
        exit
    else:
        print("Invalid Choice")
        break
    
    
    
