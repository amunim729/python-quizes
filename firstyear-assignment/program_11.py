"""
Write a program that accepts a number from a user between 1 and 10 and prints the
following triangular format.
Input from user: 4
output:
1 
22
333
4444
"""
# Agoruthm: 2 methods (string path and maths path)
# Maths path: 1 * 1 =  1, 2 * 11 =  22, 3 * 111 = 333, therefore 11 = 99/9, 111 = 999/9, therefore, n = 10^i - 1 / 9
# String path: str(i) * i

no = int(input("Choose a number (1-10): "))

# Method 1: String path
for i in range(1, no+1):
    line = str(i) * i
    print(line)

# Method 2: Maths path
for i in range(1, no+1):
    num = ((10**i) - 1) / 9
    line = str(int(i * num))
    print(line)
