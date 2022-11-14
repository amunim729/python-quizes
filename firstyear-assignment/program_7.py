"""
Write a program given a global string variable, it would allow the user to guess the
spelling of the word one letter at a time (implement the hung man game). You are not
allowed to use lists or dictionaries or tuples or any other data structure. To simplify, use a
word with non repeated letters. The number of tries for guessing is the length of the
chosen word plus one. If the same word is provided by the user, the number of tries are
not decreased.
Hint :
-> you can use a number to store found and not found letters
Eg. for instance, 1 could represent letters not found and 2 could represent words that are
found. So for the word “great” when no letter is found, the tracking number will be 11111
and when all the letters are found then the tracker number would be 22222
-> to check if a letter is in a word use the keyword “in”
-> to find the index of a letter in a word, you can use “find” function like this a=“abcd”
b=a.find(“c”) which returns b=2. An Example output:-
you are left with 6 trys
Give me a letter - a
11121 ___a_
you are left with 5 trys
Give me a letter - a
11121 ___a_
you are left with 5 trys
Give me a letter - e
11221 __ea_
you are left with 4 trys
Give me a letter - g
21221 g_ea_
you are left with 3 trys
Give me a letter - t
21222 g_eat
you are left with 2 trys
Give me a letter - i
** Nope **
you are left with 1 trys
Give me a letter - r
22222 great
you did it!!
"""
# RULES: 1 word with non repeated letters. 
# The number of tries for guessing is the length of the chosen word plus one. 
# If he got it, the number of tries are not decreased.

# ----------- HANGMAN ------------- #
word = "WORLD"
length = len(word)
chance = length + 1

placeholder = "_"*length

used = ""  # Since there is no repeated letter in the game, let us remind the user not to repeat

print("Welcome to HANGMAN Game - Text Version")
while chance != 0:
    print(placeholder)
    letter = input(f"Guess one letter: [{chance} chances left - ] ").upper()
    if len(letter) != 1:
        print("Only one letter per trial!")
        continue
    if letter in used:
        print("You have already used this letter. Try another. ")
        continue
    used += letter
    if letter in word:
        index = word.find(letter)
        print("You got it.")
        checker = ""
        for i in range(len(placeholder)):
            if i == index:
                checker += letter
            else:
                checker += placeholder[i]
        placeholder = checker

        if placeholder == word:
            print(f"Congratualtions you won. The word is {placeholder}")
            break
    else:
        chance -= 1
        if chance == 0:
            print("You have lost. Try again later!")
            break
        else:
            print("Wrong! Try again.")
