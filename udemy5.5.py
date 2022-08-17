#Guess the number
import random

tries = 0
number = random.randint(1, 50)

print("Try to guess the number between 1 and 50")

while tries < 6:
    guess = int(input("Try to guess"))
    tries += 1
    if guess < number:
        print("Too low")
    if guess > number:
        print("This number is grater")
    if guess == number:
        print("Congratulation")
        break
    if guess != number and tries == 6:
        print(f'Unfortynatle u lose this time, true number is {number}')
        break