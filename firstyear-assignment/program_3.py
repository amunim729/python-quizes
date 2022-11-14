"""
Write a program that would take the name, the age and the height of a person and
inform the user of seats allowed for them in an airplane.
3.1. If the age of a person is less than or equal to 15, they are not allowed to take the
window seat
3.2. If and only if the age of the person is greater than 20 and their height is greater
than 1.65, they are allowed to sit by the exit doors.
3.3. If and only if the age of the person is greater than 15 or less than 60, they are
allowed to seat in the middle seat
3.4. If their age is greater than 60 or less than 15, they should sit by the aisle seat
"""

# input: name, age, height  output: allowed seats
# rules: age <= 15, windows seat not allowed
# rules: age > 20 and height > 1.65, exit doors allowed
# rules: age > 15 and age < 60, middle seat alowed
# rules: age > 60 and age < 15, Aisle sit recommended

name = input("Name: ")
height = float(input("Height: "))
age = int(input("Age: "))

aisle = 1   
exit_door = 0  # allowed only for those above 20 and abpve 1.65, for others not allowed
middle = 0
windows = 1  # default allowed for all except <= 15 children

if age <= 15:
    windows = 0
if age > 20 and height > 1.65:
    exit_door = 1
if 15 < age < 60:
    middle = 1

print(f"Allowed seats for {name}: ")

if age > 60 or age < 15:
    aisle = 1
    print("*Strongly Recommended: Aisle seat*")

if exit_door == 1:
    print(" - Exit Door seat")
if middle == 1:
    print(" - Middle seat")
if windows == 1:
    print(" - Windows seat")
if aisle == 1:
    print(" - Aisle seat")
