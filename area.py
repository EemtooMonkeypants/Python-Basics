print("Welcome to Area and Perimeter!")
def area(s):
    print("The area of the square is",s**2)
def perimeter(s):
    print("The perimeter of the square is",s*4)
def area1(l, w):
    print("The area of the rectangle is",l*w)
def perimeter1(l, w):
    print("The perimeter of the rectangle is",2*l+2*w)
def area2(r):
    print("The area of the circle is",3.14*r*r)
def circumference(r):
    print("The circumference of the circle is",2*3.14*r)
count = 0
while True:
    op = int(input("Press 1 for square, 2 for rectangle, 3 for circle, or 4 for exit. "))
    if op==1:
        side = int(input("Enter the length of a side of the square."))
        area(side)
        perimeter(side)
    if op==2:
        l = int(input("Enter the length of the rectangle."))
        w = int(input("Enter the width of the rectangle."))
        area1(l,w)
        perimeter1(l,w)
    if op==3:
        r = int(input("Enter the radius of the circle."))
        area2(r)
        circumference(r)
    if op==4:
       print("Switching off...") 
       break
