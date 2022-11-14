"""
Write a program that would sequentially (not recursive) calculate the following type of
sum.
Eg:- (“^” means to the power of)
f(3)
=> it prints the following sequence and the computational result
[3 * (1)^3 + 3 * (2)^3 + 3 * (3)^3] + [2 * (1)^2 + 2 * (2)^2] + [1 * (1)^1] = 119
f(4)
=> it prints the following sequence and the computational result
[4 * (1)^4 + 4 * (2)^4 + 4 * (3)^4 + 4 * (4)^4 ]+ [3 * (1)^3 + 3 * (2)^3 + 3 * (3)^3] + [2 *
(1)^2 + 2 * (2)^2] + [1 * (1)^1] = 1535
"""

# input:a number output: sequence + result
# computation: total = 0 for each x in range(1,number+1):
#                           for each y in range(1,x+1): 
#                               total += x + (y)**x
# Sequence: [] + [] + [] = sum
# seq = str(), for x in range(1, number+1): partial_seq = "[", 
# for y in range(x, x+1): 
#      form = f"{x} + ({y})^{x}" 
#      if x == y: 
#           if x == 1: 
#               form += "] = " 
#           else: 
#               form += "] +"
#      seq += partial_seq

no = 3
total = 0
sequence = str()

for x in range(1,no+1)[::-1]:
    partial_seq = "["
    for y in range(1, x+1):
        computation = x * y**x # x + (y)**x 
        seq = f"{x} * ({y})^{x}"
        if y == x:
            if x == 1:
                seq += "] = "
            else:
                seq += "] + "
        else:
            seq += " + "
        total += computation
        partial_seq += seq
    sequence += partial_seq
sequence += str(total)

print(sequence)
