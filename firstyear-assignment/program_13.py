"""
Write a program that sequentially (not recursively) computes the first 10 summation
series produced by adding the previous summations of “setSize” given by the user.
When setSize=2 it becomes a fibonacci series. For example for sets of size 2, 3 and 4 ;
● For sets of size two (Fibonacci) => f(n)=f(n-1)+f(n-2)
● for sets of size three => f(n)=f(n-1)+f(n-2)+f(n-3)
● for sets of size four => f(n)=f(n-1)+f(n-2)+f(n-3)+f(n-4)
The outputs would look like the following (you do not need to include the addition part)
Give me set size- 3
➢ f( 0 )= 0
➢ f( 1 )= 1
➢ f( 2 )= 2
➢ f( 3 )= 0+1+2 = 3
➢ f( 4 )= 1+2+3 = 6
➢ f( 5 )= 2+3+6 = 11
➢ f( 6 )= 3+6+11 = 20
➢ f( 7 )= 6+11+20 = 37
➢ f( 8 )= 11+20+37 = 68
➢ f( 9 )= 20+37+68 = 125
- Since you are not allowed to use lists, you can use a string to hold the previous summed
values.
"""

# Algorithm
# First depending on the set size, we sort our first list of numbers
# example: setSize = 3, (0, 1, 2 are naturlly there)
# setSize = 2 (0, 1 is anturally there)
# sum = ""
# for i in range(setSize):
#   sum += f"{i}_"

# Now we can continue
# The next number is the summation of the previous (2 if setSize 2, 3 if setSize 3)
# sum = sum[:-1] (getting rid of the last _)
# total = 0
# nums = sum.split("_")[-setSize:]
# for num in nums:
#   total += int(num)
# sum += f"{total}_"  # adding it to the series, How many times we d this? Depends on the user



def calc(setsize, no=10):
    sequence = ""
    for i in range(setsize):
        sequence += f"{i}_"
    for i in range(setsize, no):
        tot = 0
        seq = sequence[:-1].split("_") # until -1, to get rid of the last _
        nums = seq[-setsize:]
        for num in nums:
            tot += int(num)
        sequence += f"{tot}_"
    return sequence[:-1]

setSize = int(input("Set Size: "))
a = calc(setSize).split("_")
i = 0
for val in a:
    print(f"f({i}) = {val}")
    i += 1
