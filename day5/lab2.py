#WAP to to guess a number between 1 to 9.
import random
target_num, guess_num = random.randint(1,10), 0
while target_num != guess_num:
    guess_num=int(input("guess a number between 1 and 10 untill you get it right:"))
print("well guessed")

# target_num=random.randint(1,10)
# guess_number=0