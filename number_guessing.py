
import random

secret_number = random.randint(1, 10)
guess = 0

print("Welcome to the Number Guessing Game!")

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
