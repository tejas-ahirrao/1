import random
number = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))
if guess == number:
    print("Correct! You guessed it!")
else:
    print(f"Wrong! The number was {number}.")
