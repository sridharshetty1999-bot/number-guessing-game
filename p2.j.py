import random
import time

def intro():
    print("What is your name?")
    return input()

def game(name):
    number = random.randint(1, 200)
    guesses = 0

    print(f"{name}, I am thinking of a number between 1 and 200")

    while guesses < 6:
        try:
            guess = int(input("Guess: "))
            guesses += 1

            if guess < number:
                print("Too low")
            elif guess > number:
                print("Too high")
            else:
                print(f"Good job {name}! You guessed it in {guesses} guesses!")
                return
        except ValueError:
            print("Please enter a number")

    print(f"Sorry! The number was {number}")

playagain = "yes"
while playagain.lower() in ("yes", "y"):
    name = intro()
    game(name)
    playagain = input("Play again? ")
