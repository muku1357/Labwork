#Write a Python program that accepts a string and calculate the number of digits and letters

str = "Helloworldcomputing hello again1"
digit=letter=0
for ch in str:
   if ch.isdigit():
      digit=digit+1
   elif ch.isalpha():
      letter=letter+1
   else:
      pass
print("Letters:", letter)
print("Digits:", digit)
