import os
clear = lambda: os.system('cls')
clear()

print("please enter the number of the the function or type help to find the functions")
print("1 to find the diameter of the circle from the radius")
print("2 to find the radius from the diameter of the circle")
print("3 to find the perimeter of the circle from the diameter of the circle")
print("4 to find the perimeter of the circle from the radius of the circle")
print("5 to find the space of the circle from the radius of the circle")
print("6 to find the space of the circle from the diameter of the circle")
print("7 to find the space of the triangle")
print("8 to find the perimeter of the triangle")
print("9 to find the perimeter of the square")
print("10 to find the space of the square")
print("11 to find the space of the 3dsquare")
print("12 to find the space of the cylinder")

c = input("")
if c == '1' :
    print("Please enter the radius of the circle")
    gh = int(input(""))
    print("this is the diameter of the circle")
    print(gh * 2)

if c == '2' :
    print("please enter the diameter of the circle")
    gh = int(input(""))
    print("this is the diameter of the circle")
    print(gh / 2)

if c == '3' :
    print("please enter the diameter of the circle to find the perimeter of the circle")
    gh = int(input(""))
    print("this is the perimeter of the circle")
    print(gh * 3.14)

if c == '4' :
    print("please enter the radius of the circle to find the perimeter of the circle")
    gh = int(input(""))
    print(" this is the perimeter of the circle")
    print(2 * gh * 3.14)

if c == '5' :
    print("please enter the radius of the circle to find the space of the circle")
    gh = float(input(""))
    print("this is the space of the circle")
    print(gh * gh * 3.14)

if c == '6' :
    print("please enter the diameter of the circle to find the space of the circle")
    gh = int(input(""))
    ghj = int(gh) / 2
    print("this is the space of the circle")
    print(gh * gh * 3.14)

if c == '7' :
    print("please enter the height and the base")
    gh = int(input(""))
    print("please enter the height of the triangle attitude")
    ghh = int(input(""))
    print("please the width of the triangle base")
    print(1 / 2 * gh * ghh)
    print("this is the space of the triangle")

if c == '8' :
    print("please enter the height the base and the vertex the triangle")
    print("please enter the width of the triangle base")
    gh = int(input(""))
    print("please the height of the triangle attitude")
    ghh = int(input(""))
    print("please enter of how long the triangle vertex is")
    ghj = int(input(""))
    print(gh + ghh + ghj)
    print("this is the perimeter of the triangle")

if c == '9' :
    print("please enter the width and the height of the square to find the perimeter of the square")
    print("please enter the width of the square")
    gh = int(input(""))
    print("please enter the height of the square")
    ghh = int(input(""))
    print("this is the perimeter of the square")
    print((gh * 2) + (ghh * 2))

if c == '10' :
    print("please enter the width and the height of the square to find the space of the square")
    print("please enter the width of the square")
    gh = int(input(""))
    print("please enter the height of the square")
    ghh = int(input(""))
    print("this is the space of the square")
    print(gh* ghh)

if c == '11' :
    print("now enter the width height and how long the square the 3dsquare is")
    print(".")
    print("please enter the width of the square")
    gh = int(input(""))
    print("please enter the height of the square")
    ghh = int(input(""))
    print("please enter how long the square is")
    ghj = int(input(""))
    print("this is the space of the 3dsquare ")
    print(gh *ghh *ghj)
    
if c == '12' :
    print("now enter the width height and how long the the radius is")
    print("please enter the radius")
    gh = int(input(""))
    print("please enter the height of the cylinder")
    ghh = int(input(""))
    print(3.14 * gh * ghh)

if c == '13' :
    print("")

if c == "help" :
    print("1 to find the diameter of the circle from the radius")
    print("2 to find the radius from the diameter of the circle")
    print("3 to find the perimeter of the circle from the diameter of the circle")
    print("4 to find the perimeter of the circle from the radius of the circle")
    print("5 to find the space of the circle from the radius of the circle")
    print("6 to find the space of the circle from the diameter of the circle")
    print("7 to find the space of the triangle")
    print("8 to find the perimeter of the triangle")
    print("9 to find the perimeter of the square")
    print("10 to find the space of the square")
    print("11 to find the space of the 3dsquare")
    print("12 to find the space of the cylinder")