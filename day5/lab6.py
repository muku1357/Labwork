#Write a Python program to count the number of even andodd numbers from a series of numbers.

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
