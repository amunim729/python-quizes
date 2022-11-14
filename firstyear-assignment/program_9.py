"""
Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

n = input("Enter an integer: ")
# Method one - eval is always associated with high security risk
comp = eval(f"{n} + {n}{n} + {n}{n}{n}")
print(comp)

# Method two -  with lesser security risk
n = int(n)
nn = n * 11
nnn = n * 111
comp = n + nn + nnn
print(comp)
