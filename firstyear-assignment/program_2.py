# Write a program that would calculate the mean of a sequence of numbers received from
# a user one at a time until the person inserts the key term “done”.

total = 0
frequency = 0

while True:
    no = input("Enter a number ('done' when done): ")
    if no.lower() == "done":
        if frequency != 0: # Avoiding Divide by Zero Exception
            print(f"The mean is {total/frequency}") 
            break
        else:
            print("You have not yet entered any number.")
            continue
    else:
        no = float(no)
        total += no
        frequency += 1

