import math
def Area_of_Equilateral_Triangle():
        a=int(input("Enter the Side of the Equilateral Triangle -"))
        c=0.4*a**2
        return c
def Height_of_Equilateral_Triangle():
        a=int(input("Enter the Side of the Equilateral Triangle -"))
        c=0.8*a
        return c
def Perimeter_of_Equilateal_Triangle():
        a=int(input("Enter the Side of the Equilateral Triangle -"))
        c=3*a
        return c
def Area_of_Isosceles_Triangle():
        a=float(input("Enter the Side of the Isosceles Triangle where a has the same side -"))
        b=float(input("Enter the base of the Isosceles Triangle -"))
        n=math.sqrt(a**2-b**2//4)
        c=b//2*n
        return c
def Height_of_Isosceles_Triangle():
        a=float(input("Enter the Side of the Isosceles Triangle where a has the same side -"))
        b=float(input("Enter the base of the Isosceles Triangle -"))
        n=math.sqrt(a**2-b**2//4)
        c=n
        return c
def Perimeter_of_Isosceles_Triangle():
        a=int(input("Enter the Side of the Isosceles Triangle where a has the same side -"))
        b=int(input("Enter the base of the Isosceles Triangle -"))
        c=2*a+b
        return c
def Area_of_Scalence_Triangle_BH():
        b=int(input("Enter the base of the Scalence Triangle -"))
        h=int(input("Enter the Height of the Scalence Triangle -"))
        c=0.5*b*h
        return c
def Area_of_Scalence_Triangle_ABC():
        a=float(input("Enter the First Side of the Scalence Triangle -"))
        b=float(input("Enter the Second Side of the Scalence Triangle -"))
        c=float(input("Enter the Third Side of the Scalence Triangle - "))
        s=(a+b+c)//2
        n=math.sqrt(s*(s-a)*(s-b)*(s-c))
        d=n
        return d
def Perimeter_of_Scalence_Triangle():
        a=int(input("Enter the First Side of the Scalence Triangle -"))
        b=int(input("Enter the Second Side of the Scalence Triangle -"))
        c=int(input("Enter the Third Side of the Scalence Triangle - "))
        d=a+b+c
        return d
def Area_of_Rectangle():
        l=int(input("Enter the Length of the Rectangle -"))
        b=int(input("Enter the Breadth of the Rectangle -"))
        c=l*b
        return c
def Perimeter_of_Rectangle():
        l=int(input("Enter the Length of the Rectangle -"))
        b=int(input("Enter the Breadth of the Rectangle -"))
        c=2*(l+b)
        return c
def Diameter_of_Rectangle():
        l=float(input("Enter the Length of the Rectangle -"))
        b=float(input("Enter the Breadth of the Rectangle -"))
        n=math.sqrt(l**2+b**2)
        c=n
def Area_of_Square_A():
        a=int(input("Enter the Side of the Square -"))
        c=a*a
        return c
def Area_of_Square_D():
        d=int(input("Enter the Diameter or Diagonal of the Square -"))
        c=d**2//4
        return c
def Perimeter_of_Square():
        a=int(input("Enter the Side of the Square -"))
        c=4*a
        return c
def Diameter_of_Square():
        a=int(input("Enter the Side of the Square -"))
        c=a*1.4142
        return c
def Circumference_of_Circle():
        r=int(input("Enter the Radius of the Circle -"))
        c=2*3.14*r
        return c
def Area_of_Circle():
        r=int(input("Enter the Radius of the Circle -"))
        c=3.14*r**2
        return c
def Area_of_Parallelogram():
        b=int(input("Enter the base of the Parallelogram -"))
        h=int(input("Enter the Height of the Parallelogram -"))
        c=b*h
        return c
def Perimeter_of_Parallelogram():
        b=int(input("Enter the base of the Parallelogram -"))
        a=int(input("Enter the Side of the Parallelogram -"))
        c=2*(a+b)
        return c
def Area_of_Rhombus():
        d1=int(input("Enter the First Diameter of the Rhombus -"))
        d2=int(input("Enter the Second Diameter of the Rhombus -"))
        c=0.5*d1*d2
        return c
def Perimeter_of_Rhombus():
        a=int(input("Enter the Side of the Rhombus -"))
        c=4*a
        return c
def Area_of_Trapezium():
        a=int(input("Enter the first parallel side of the Trapezium -"))
        b=int(input("Enter the Second Paralel side of the Trapezium -"))
        h=int(input("Enter the Height of the Trapezium -"))
        c=0.5*h*(a+b)
        return c
def Perimeter_of_Trapezium():
        a=int(input("Enter the First Side of the Trapezium -"))
        b=int(input("Enter the Second Side of the Trapezium -"))
        c=int(input("Enter the Third Side of the Trapezium - "))
        d=int(input("Enter the Fourth Side of the Trapezium -"))
        p=a+b+c+d
        return p
def CSA_of_Cuboid():
        l=int(input("Enter the Length of the Cuboid -"))
        b=int(input("Enter the Breadth of the Cuboid -"))
        h=int(input("Enter the Height of the Cuboid -"))
        c=2*h*(l+b)
        return c
def TSA_of_Cuboid():
        l=int(input("Enter the Length of the Cuboid -"))
        b=int(input("Enter the Breadth of the Cuboid -"))
        h=int(input("Enter the Height of the Cuboid -"))
        c=2*((l*b)+(b*h)+(h*l))
        return c
def Volume_of_Cuboid():
        l=int(input("Enter the Length of the Cuboid -"))
        b=int(input("Enter the Breadth of the Cuboid -"))
        h=int(input("Enter the Height of the Cuboid -"))
        c=l*b*h
        return c
def Diameter_of_Cuboid():
        l=float(input("Enter the Length of the Cuboid -"))
        b=float(input("Enter the Breadth of the Cuboid -"))
        h=float(input("Enter the Height of the Cuboid -"))
        n=math.sqrt(l**2+b**2+h**2)
        c=math.sqrt(l**2+b**2+h**2)
        return c
def CSA_of_Cube():
        a=int(input("Enter the Side of the Cube -"))
        c=4*a**2
        return c
def TSA_of_Cube():
        a=int(input("Enter the Side of the Cube -"))
        c=6*a**2
        return c
def Volume_of_Cube():
        a=int(input("Enter the Side of the Cube -"))
        c=a**3
        return c
def Diameter_of_Cube():
        a=int(input("Enter the Side of the Cube -"))
        c=a*1.73
        return c
def CSA_of_Cylinder():
        r=int(input("Enter the Radius of the Cylinder -"))
        h=int(input("Enter the Height of the Cylinder -"))
        c=2*3.14*r*h
        return c
def TSA_of_Cylinder():
        r=int(input("Enter the Radius of the Cylinder -"))
        h=int(input("Enter the Height of the Cylinder -"))
        c=2*3.14*r*(h+r)
        return c
def Volume_of_Cylinder():
        r=int(input("Enter the Radius of the Cylinder -"))
        h=int(input("Enter the Height of the Cylinder -"))
        c=3.14*r**2*h
        return c
def CSA_of_Cone():
        r=int(input("Enter the Radius of the Cone -"))
        l=int(input("Enter the Slant Height(L) of the Cone -"))
        c=2*3.14*r*l
        return c
def TSA_of_Cone():
        r=int(input("Enter the Radius of the Cone -"))
        l=int(input("Enter the Slant Height(L) of the Cone -"))
        c=3.14*r*(l+r)
        return c
def Volume_of_Cone():
        r=int(input("Enter the Radius of the Cone -"))
        h=int(input("Enter the Height of the Cone -"))
        c=0.3*3.14*r**2*h
        return c
def Slant_Height_of_Cone():
        r=float(input("Enter the Radius of the Cone -"))
        h=float(input("Enter the Height of the Cone -"))
        n=math.sqrt(h**2+r**2)
        c=n
        return c
def TSA_of_Sphere():
        r=int(input("Enter the Radius of the Sphere -"))
        c=4*3.14*r**2
        return c
def Volume_of_Sphere():
        r=int(input("Enter the Radius of the Sphere -"))
        c=1.3*3.14*r**3
        return c
def CSA_of_Hemisphere():
        r=int(input("Enter the Radius of the Hemisphere -"))
        c=2*3.14*r**2
        return c
def TSA_of_Hemisphere():
        r=int(input("Enter the Radius of the Hemisphere -"))
        c=3*3.14*r**2
        return c
def Volume_of_Hemisphere():
        r=int(input("Enter the Radius of the Hemisphere -"))
        c=0.6*3.14*r**3
        return c

def Mainmenu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    
        
def shapes_menu2d():
    while shapes!=8:
                print("**************************__ALL_2D_SHAPES__**************************")
                print("1. Triangles ( Equilateral Triangle , Isosceles Triangle , Scalence Triangle ) -")
                print("2. Rectangle -")
                print("3. Square -")
                print("4. Circle -")
                print("5. Parallelogram -")
                print("6. Rhombus -")
                print("7. Trapezium -")
                print("8. Exit")
                print("______________________________________________________________________")
                shapes=int(input("Enter your choice(1 to 8) -"))
def shapes_menu3d():
     while shapes!=7:
                print("**************************__ALL_3D_SHAPES__**************************")
                print("1. Cuboid -")
                print("2. Cube -")
                print("3. Cylinder -")
                print("4. Cone -")
                print("5. Sphere -")
                print("6. Hemishere -")
                print("7. Exit")
                print("______________________________________________________________________")
                shapes=int(input("Enter your choice(1 to 7) -"))
def triangle_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while triangle!=4:
                        print("*************__SELECT_TYPE_OF_TRIANGLE__************")
                        print("1. Equilateral Triangle -")
                        print("2. Isosceles Triangle -")
                        print("3. Scalence Triangle -")
                        print("4. Exit")
                        print("_____________________________________________________")
                        triangle=int(input("Enter your choice(1 to 4) -"))
                        if triangle==1:
                            while ahp!=4:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. Area -")
                                print("2. Height -")
                                print("3. Perimeter -")
                                print("4. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 4) -"))
                                if ahp==1:
                                    x=Area_of_Equilateral_Triangle()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=Height_of_Equilateral_Triangle()
                                    print("Answer is",x)
                                elif ahp==3:
                                    x=Perimeter_of_Equilateal_Triangle()
                                    print("Answer is",x)
                                elif ahp==4:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
                        elif triangle==2:
                            while ahp!=4:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. Area -")
                                print("2. Height -")
                                print("3. Perimeter -")
                                print("4. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 4) -"))
                                if ahp==1:
                                    x=Area_of_Isosceles_Triangle()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=Height_of_Isosceles_Triangle()
                                    print("Answer is",x)
                                elif ahp==3:
                                    x=Perimeter_of_Isosceles_Triangle()
                                    print("Answer is",x)
                                elif ahp==4:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid choice")
                                    break
                        elif triangle==3:
                            while ahp!=4:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. Area -")
                                print("2. Perimeter -")
                                print("3. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 3) -"))
                                if ahp==1:
                                    while bh!=3:
                                        print("*************__ENTER_WHICH_ELEMENTS_DO_YOU_HAVE__************")
                                        print("1. Base and Height -")
                                        print("2. All Three Sides -")
                                        print("3. Exit")
                                        print("______________________________________________________________")
                                        bh=int(input("Enter your choice(1 to 3) -"))
                                        if bh==1:
                                            x=Area_of_Scalence_Triangle_BH()
                                            print("Answer is",x)
                                        elif bh==2:
                                            x=Area_of_Scalence_Triangle_ABC()
                                            print("Answer is",x)
                                        elif bh==3:
                                            print("Program Closed")
                                            exit
                                        else:
                                            print("Invalid Choice")
                                            break
                                elif ahp==2:
                                    x=Perimeter_of_Scalence_Triangle()
                                    print("Answer is",x)
                                elif ahp==3:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Inavlid Choice")
                                    break
def Rectangle_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=4:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. Area -")
                                print("2. Perimeter -")
                                print("3. Diagonal or Diameter -")
                                print("4. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 4) -"))
                                if ahp==1:
                                    x=Area_of_Rectangle()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=Perimeter_of_Rectangle()
                                    print("Answer is",x)
                                elif ahp==3:
                                    x=Diameter_of_Rectangle()
                                    print("Answer is",x)
                                elif ahp==4:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Square_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=4:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. Area -")
                                print("2. Perimeter -")
                                print("3. Diagonal or Diameter -")
                                print("4. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 4) -"))
                                if ahp==1:
                                    while d!=3:
                                        print("*************__ENTER_WHICH_ELEMENTS_DO_YOU_HAVE__************")
                                        print("1. Sides -")
                                        print("2. Diameter or Dagonals -")
                                        print("3. Exit")
                                        print("______________________________________________________________")
                                        d=int(input("Enter your choice(1 to 3) -"))
                                        if d==1:
                                            x=Area_of_Square_A()
                                            print("Answer is",x)
                                        elif d==2:
                                            x=Area_of_Square_D()
                                            print("Answer is",x)
                                        elif d==3:
                                            print("Program closed")
                                            exit
                                        else:
                                            print("Invalid Choice")
                                            break
                                elif ahp==2:
                                    x=Perimeter_of_Square()
                                    print("Answer is",x)
                                elif ahp==3:
                                    x=Diameter_of_Square()
                                    print("Answer is",x)
                                elif ahp==4:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Circle_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=3:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. Area -")
                                print("2. Circumference -")
                                print("3. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 3) -"))
                                if ahp==1:
                                    x=Area_of_Circle()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=Circumference_of_Circle()
                                    print("Answer is",x)
                                elif ahp==3:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Parallelogram_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=3:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. Area -")
                                print("2. Perimeter -")
                                print("3. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 3) -"))
                                if ahp==1:
                                    x=Area_of_Parallelogram()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=Perimeter_of_Parallelogram()
                                    print("Answer is",x)
                                elif ahp==3:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Rhombus_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=3:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. Area -")
                                print("2. Perimeter -")
                                print("3. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 3) -"))
                                if ahp==1:
                                    x=Area_of_Rhombus()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=Perimeter_of_Rhombus()
                                    print("Answer is",x)
                                elif ahp==3:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Trapezium_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=3:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. Area -")
                                print("2. Perimeter -")
                                print("3. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 3) -"))
                                if ahp==1:
                                    x=Area_of_Trapezium()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=Perimeter_of_Trapezium()
                                    print("Answer is",x)
                                elif ahp==3:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Cuboid_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=5:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. C.S.A.(Curved Surface Area) -")
                                print("2. T.S.A.(Total Surface Area) -")
                                print("3. Volume ")
                                print("4. Diagonal or Diameter -")
                                print("5. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 5) -"))
                                if ahp==1:
                                    x=CSA_of_Cuboid()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=TSA_of_Cuboid()
                                    print("Answer is",x)
                                elif ahp==3:
                                    x=Volume_of_Cuboid()
                                    print("Answer is",x)
                                elif ahp==4:
                                    x=Diameter_of_Cuboid()
                                    print("Answer is",x)
                                elif ahp==5:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Cube_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=5:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. C.S.A.(Curved Surface Area) -")
                                print("2. T.S.A.(Total Surface Area) -")
                                print("3. Volume ")
                                print("4. Diagonal or Diameter -")
                                print("5. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 5) -"))
                                if ahp==1:
                                    x=CSA_of_Cube()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=TSA_of_Cube()
                                    print("Answer is",x)
                                elif ahp==3:
                                    x=Volume_of_Cube()
                                    print("Answer is",x)
                                elif ahp==4:
                                    x=Diameter_of_Cube()
                                    print("Answer is",x)
                                elif ahp==5:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Cylinder_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=4:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. C.S.A.(Curved Surface Area) -")
                                print("2. T.S.A.(Total Surface Area) -")
                                print("3. Volume ")
                                print("4. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 4) -"))
                                if ahp==1:
                                    x=CSA_of_Cylinder()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=TSA_of_Cylinder()
                                    print("Answer is",x)
                                elif ahp==3:
                                    x=Volume_of_Cylinder()
                                    print("Answer is",x)
                                elif ahp==4:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Cone_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=5:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. C.S.A.(Curved Surface Area) -")
                                print("2. T.S.A.(Total Surface Area) -")
                                print("3. Volume ")
                                print("4. Slant Height(L) -")
                                print("5. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 5) -"))
                                if ahp==1:
                                    x=CSA_of_Cone()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=TSA_of_Cone()
                                    print("Answer is",x)
                                elif ahp==3:
                                    x=Volume_of_Cone()
                                    print("Answer is",x)
                                elif ahp==4:
                                    x=Slant_Height_of_Cone()
                                    print("Answer is",x)
                                elif ahp==5:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Sphere_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=3:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. T.S.A.(Total Surface Area) -")
                                print("2. Volume ")
                                print("3. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 3) -"))
                                if ahp==1:
                                    x=TSA_of_Sphere()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=Volume_of_Sphere()
                                    print("Answer is",x)
                                elif ahp==3:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break
def Hemisphere_menu():
    shapes=0
    d=0
    ahp=0
    bh=0
    triangle=0
    dimension=0
    while ahp!=4:
                                print("**************__SELECT_WHICH_DO_YOU_WANT_TO_PERFORM__**************")
                                print("1. C.S.A.(Curved Surface Area) -")
                                print("2. T.S.A.(Total Surface Area) -")
                                print("3. Volume ")
                                print("4. Exit")
                                print("____________________________________________________________________")
                                ahp=int(input("Enter your choice(1 to 4) -"))
                                if ahp==1:
                                    x=CSA_of_Hemisphere()
                                    print("Answer is",x)
                                elif ahp==2:
                                    x=TSA_of_Hemisphere()
                                    print("Answer is",x)
                                elif ahp==3:
                                    x=Volume_of_Hemisphere()
                                    print("Answer is",x)
                                elif ahp==4:
                                    print("Program Closed")
                                    exit
                                else:
                                    print("Invalid Choice")
                                    break


shapes=0
d=0
ahp=0
bh=0
triangle=0
dimension=0
Mainmenu()
while dimension!=3:
    print("***********__MATHEMATICAL_ARITHMETIC_PROBLEM_SOLVER__***********")
    print("1. Calculations on 2D Shapes -")
    print("2. Calculations on 3D Shapes -")
    print("3. Exit")
    print("________________________________________________________________")
    dimension=int(input("Enter your choice(1 to 3) -"))
    if dimension==1:
        while shapes!=8:
            print("**************************__ALL_2D_SHAPES__**************************")
            print("1. Triangles ( Equilateral Triangle , Isosceles Triangle , Scalence Triangle ) -")
            print("2. Rectangle -")
            print("3. Square -")
            print("4. Circle -")
            print("5. Parallelogram -")
            print("6. Rhombus -")
            print("7. Trapezium -")
            print("8. Exit")
            print("______________________________________________________________________")
            shapes=int(input("Enter your choice(1 to 8) -"))
            if shapes==1:
                triangle_menu()
            elif shapes==2:
                Rectangle_menu()
            elif shapes==3:
                Square_menu()
            elif shapes==4:
                Circle_menu()
            elif shapes==5:
                Parallelogram_menu()
            elif shapes==6:
                Rhombus_menu()
            elif shapes==7:
                Trapezium_menu()
    elif dimension==2:
        while shapes!=7:
            print("**************************__ALL_3D_SHAPES__**************************")
            print("1. Cuboid -")
            print("2. Cube -")
            print("3. Cylinder -")
            print("4. Cone -")
            print("5. Sphere -")
            print("6. Hemishere -")
            print("7. Exit")
            print("______________________________________________________________________")
            shapes=int(input("Enter your choice(1 to 7) -"))
            if shapes==1:
                Cuboid_menu()
            elif shapes==2:
                Cube_menu()
            elif shapes==3:
                Cylinder_menu()
            elif shapes==4:
                Cone_menu()
            elif shapes==5:
                Sphere_menu()
            elif shapes==6:
                Hemisphere_menu()
    elif dimension==3:
            print("Program Closed")
            exit
    else:
        print("Invalid Choice")
        break



