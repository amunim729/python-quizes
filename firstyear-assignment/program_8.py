"""
Write a program that accepts a string from a user and checks if the string provided is
symmetrical or not. Do this until the user types done.
Please enter a string: abeba
String is symmetrical
Please enter a string: abebe
String is not symmetrical
Please enter a string: done
Exit
"""

def symmetrical(the_word):
    """
    Method 1
    """
    symm = ""
    the_word = the_word.lower()
    length = len(the_word)
    for i in range(1, length + 1):
        symm += the_word[length - i]
    return symm == the_word

def is_sym(the_word):
    """
    Method 2: using string slicing
    """
    the_word = the_word.lower()
    return the_word == the_word[::-1]

print("Symmetrical Word Checker\n done - to exit")
while True:
    word = input("String: ")
    if word == 'done':
        print("Exit")
        break
    print(f'{word} is symmetrical.' if is_sym(word) else f'{word} is not symmetrical.')
