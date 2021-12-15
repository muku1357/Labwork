#Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)

# Python program to convert temperature from Celsius to Fahrenheit
 
celsius = float(input("Enter temperature in celsius:"))
 
fahrenheit = (celsius * 9/5) + 32
 
print('%.2f Celsius is : %0.2f Fahrenheit' %(celsius, fahrenheit))

'''# Python program to convert Fahrenheit to Celsius
 
fahrenheit = float(input("Enter temperature in fahrenheit:"))
 
celsius = (fahrenheit - 32) * 5/9
 
print('%.2f Fahrenheit is : %0.2f Celsius' %(fahrenheit, celsius))'''
