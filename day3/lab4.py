4.# Given three integers, print the smallest one. (Three integers should be user input) 
A =int(input("enter the first number"))
B = int(input("enter the second number"))
C =int(input("enter the third number"))
if (A>B & A>C):
    print("A is greatest")
elif (B>A & B>C):
    print("B is greatest")
else:
    print("C is greatest")
