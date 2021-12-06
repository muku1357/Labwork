#Give a n-digit number.Find the the sum of digits.
A = int(input("enter the First number"))
sum = 0
for digit in str(A):
 sum += int(digit) 
 print(sum)