print("Welcome to calculator!")
def sum(a,b):
    print(a+b)
def difference(a,b):
    print(a-b)
def product(a,b):
    print(a*b)
def quotient(a,b):
    print(a/b)
count = 0
while count==0:
    op = int(input("Press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, or 5 for exit. "))
    if op==1:
        num1 = int(input("Enter the first number you would like to add."))
        num2 = int(input("Enter the second number you would like to add."))
        sum(num1, num2)
    elif op==2:
        num1 = int(input("Enter the first number you would like to subtract."))
        num2 = int(input("Enter the second number you would like to subtract."))
        difference(num1, num2)
    elif op==3:
        num1 = int(input("Enter the first number you would like to multiply."))
        num2 = int(input("Enter the second number you would like to multiply."))
        product(num1, num2)
    elif op==4:
        num1 = int(input("Enter the first number you would like to divide."))
        num2 = int(input("Enter the second number you would like to divide."))
        quotient(num1, num2)
    elif op==5:
        print("Switching off the calculator.")
        break
