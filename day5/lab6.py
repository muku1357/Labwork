#Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = (11, 22, 33, 44, 55, 66, 77, 88, 89)
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
#WAP to print to count the number of even or odd number from the series of number
l = [2,4,6,10, 21, 4, 45, 66, 93, 1,11,31] 

even, odd= 0, 0

for i in l: 

    if i % 2 == 0: 

        even += 1

    else: 

        odd+= 1          

print("Even : ", even) 

print("Odd : ", odd)

 
