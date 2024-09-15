for i in range(10): 
    print(i)
for i in range(0, 10, 2):
    print(i)
for i in range(1, 10, 2):
    print(i)
n = int(input("Enter a number: "))
for i in range(1, n, 1):
    print(i)
sum = 0
for i in range(n+1):
    sum = sum+i
print("The sum of "+str(n)+" numbers is "+str(sum))
print("The sum of",n,"numbers is",sum)
print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2%3)       #modulus
print(2//3)      #divides the number and prints the quotient but no decimals
print(2**3)      #to the power of
print("Hi "*2)
print(2>3)
print(5>3)
print(4==4)
print(4!=4)
print(4<=4)
print(4>=5)