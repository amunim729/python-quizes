from os import system  # to keep the screen clean
from random import choices # to choose a random word

# SIMILAR TO HANGMAN

f =  open("words.txt", "r")  # open the words list
dictionary = f.readlines()  # read each line and store it in a list
for i in range(len(dictionary)):
    dictionary[i-1] = dictionary[i-1].replace("\n", "").upper()  # cleaning each word in the list, and converting them to upper case for conviniency
f.close() # close the file
the_word = choices(dictionary)[0]  # choose a random word
the_word_e = list(the_word)  # convert each letter in the word to a list
length = len(the_word)  # get the length of the word
chances = length - 1  # number of trials to guess
guessed = list("_" * length)  # place holder
system("cls")  # let us clean the place
print("  --- Guess the letters Game --- ")

while (chances != 0 and guessed != list(the_word)):
    print(" ".join(guessed))  # print our place holder
    letter = input(f"Guess the letter - {chances} chances left: ").upper()  # accept input in appropriate format
    if len(letter) != 1:  # Make sure you accept only one letter
        system("cls") 
        print("Only one letter per chance allowed. ")
        continue
    if letter in the_word and letter in the_word_e: # GOT IT WRITE
        system("cls")
        print("You got it right")  
        guessed[the_word_e.index(letter)] = letter
        the_word_e[the_word_e.index(letter)] = "_"
        if guessed == list(the_word):  # CHECK IF HE WON
            system("cls")
            print(f"You won! The word is {the_word.capitalize()}.")
            break
        continue
    chances -= 1
    if chances == 0: # PRINT OUT A NOTICE
        print(f"You are out of luck. The word was {the_word.capitalize()}.")
        break
    system("cls")
    print("Wrong! Try again!")  # IF THE LOOP REACHES HERE THE PERSON HAD PROBABLY A WRONG Guess

# And it is done:
