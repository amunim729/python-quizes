"""
Write a program that accepts a number from the user between 1 and 10 and prints n
number of lines of the following pattern.
Input from user:7
output:
      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *
"""

# Algorithm
# Last line no space
# Last-1 line 1 space
# Last - 2 line 2 space
# First = (no_of_lines-1) space

lines = 7 #int(input("Lines: (1-9) "))
assert 1 <= lines <= 10
i = lines - 1
for line in range(1, lines + 1):
    l = " "*i + "* "*line
    i -= 1
    print(l)
