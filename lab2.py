2. #WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
A = int(input("enter the marks of science"))
B = int(input("enter the marks of maths"))
C = int(input("enter the marks of social"))
D = int(input("enter the marks of Nepali"))
total_marks = A + B + C + D
print("total marks is {total marks}")
Percentage = total_marks/4
print("the percentage is {percentage}")
if Percentage > 70:
    print("you scored dictintion")
elif Percentage > 60:
    print("you scored first division")
elif Percentage > 40:
    print("you scored pass marks")
else:
    print("you are fail")