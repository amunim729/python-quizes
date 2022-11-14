"""
Write a program that does the following kind of computation given two numbers
- For Example given 15 and 20
- It would produce ->
- 1 * 20 = 20
- 3 * 17 = 51
- 5 * 14 = 70
- 7 * 11 = 77
- 9 * 8 = 72
- 11 * 5 = 55
- 13 * 2 = 26
- Done
"""

# Solution
# First number starts from one, increases by two
# Second number starts from itself, decreases by three
# stops if either if the first number is reached or the second number reaches 1

no_1 = 15
no_2 = 20

init = 1

while (init <= no_1 and no_2 >= 1):
    print(f"{init} * {no_2} = {init*no_2}")
    init += 2
    no_2 -=3

print("Done")
