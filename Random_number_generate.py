import random
def random_no_generater():
    a=random.randint(1,6)
    print("The Number on the Dice is -",a)

def main():
    n=input("Enter y to start the generating a random number -")
    while n=='y':
        random_no_generater()
        print("\n")
        print("press y to again roll the dice.")
        n=input("Do you want to roll the dice -")
main()
