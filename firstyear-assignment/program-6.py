"""
Write a program that would take a number from a user and prints out the multiplication
table of the number upto a random number between an interval of your choosing. and
then check if the multiple is a perfect square ( is a square of another number or has an
integer square root) and print out “it is perfect square” next to it or if it is a 3rd root of any
number, it prints “ it is a perfect 3rd root”. It would give the user a random amount of
chances for each run to provide a number. Example output ->
you have 2 chances
Give me a number - 6
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36 => it is a perfect square of 6
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
Give me a number - 4
4 * 1 = 4 => it is a perfect square of 2
4 * 2 = 8 => it is a perfect third root 2
4 * 3 = 12
4 * 4 = 16 => it is a perfect square of 4
4 * 5 = 20
4 * 6 = 24
"""

def perfect_square(no):
    """ Perfect square checker: How it works?  
    1. Calculate the number's square root
    2. Round it to 0 decimal point - a perfect square won't be affected, but others will
    3. Square it back and check if their integers are equal. and you get True or False
    4. if True and it is a perfect square, just return its root, else, return False
    """
    x = no == int(round((no**0.5)) ** 2)
    if not x:
        return x
    else:
        return int(round((no**0.5)))

def perfect_cube(no):
    """ Perfect Cube checker: How it works?  
    1. Calculate the number's cube root no**(1/3)
    2. Round it to 0 decimal point - a perfect cube won't be affected, but others will
    3. Cube it back and check if their integers are equal. and you get True or False
    4. if True and it is a perfect cube, just return its root, else, return False
    """

    x = no == int(round(no**(1/3)) ** 3)
    if not x:
        return x
    else:
        return int(round(no**(1/3)))

from random import randint

chances = randint(1, 3)
end = randint(5, 8)
print(f"You have {chances} chances.")
while chances != 0:
    number = int(input("Give me a number: "))
    for i in range(1, end+1):
        tot = number * i
        result = f"{number} * {i} = {tot} "
        result += "" if not perfect_cube(tot) else f" => perfect third root of {perfect_cube(tot)}"
        result += "" if not perfect_square(tot) else f" => perfect square root of {perfect_square(tot)}"
        print(result)
    chances -= 1
