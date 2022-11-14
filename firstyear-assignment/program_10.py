"""
Write a program that accepts n (a number) from a user and generate n-digit password
with only numbers.
Input from user: 6
Output: 589452
"""
n = int(input("number of digits: "))
password = ""

from random import randint

for _ in range(n):
    password += str(randint(0, 9))

print(password)
