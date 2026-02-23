Arr=[10,20,30,40,12,11]
def lshift(Arr,n):
    List=[]
    for i in range(n,len(Arr)):
        List.append(Arr[i])
    for i in range(0,n):
        List.append(Arr[i])
    print(List)
lshift(Arr,4)
