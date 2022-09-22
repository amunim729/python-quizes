from random import randint
from os import system

# Guess the Number Game - The first quiz

no = randint(1,100) # Chooses a random number for the game
chances = 5  # The chance you give them
system("cls") # Let us have a clear screen - for linux system use: system("clear")
print("   NUMBER GUESSER GAME   ")   # Don't we need a title?
while chances != 0:
    num = int(input("Guess the number: (1-100)  - "))   # Accepting the input
    if num == no:  # winning conditions
        print(f"Yayy!, you won. The no is {no}")
        break
    elif num < no:  # give 'em the hints
        system("cls")
        print(f"You guessed slightly lower... {chances - 1} chances left")
    elif num > no:  # hints again
        system("cls")
        print(f"You guessed slightly higher... {chances - 1} chances left")
    chances -= 1  # As long as the person does not win, the loop will continue to here, where the total chances will reduce
    if chances == 0:  # the loop will break eventually, but don't we need to inform the player about the answer?
        system("cls")
        print(f"You are out of chances, the number was {no}")
