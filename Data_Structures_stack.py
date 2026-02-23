def push(stk,x):                
    stk.append(x)
    top=len(stk)-1

    
def pop(stk):
    if stk==[]:
        return "UNDERFLOW!"
    else:
        t=stk.pop()
        top=len(stk)-1
        print("Removed Value or Item from the list -",t)

        
def display(stk):
    if stk==[]:
        print("UNDERFLOW! Stack is Empty")
    else:
        top=len(stk)-1
        print("Displayinig the Data-")
        for i in range(top,-1,-1):
            print(stk[i])

l=[]
push(l,5)
push(l,8)
push(l,8)
pop(l)
push(l,2)
pop(l)
push(l,5)
pop(l)
pop(l)
pop(l)
push(l,1)
pop(l)
