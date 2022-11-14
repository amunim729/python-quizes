"""
Write a program that asks the name of a student and then it asks for the father’s name of
the student if you know it then the father name of the father’s name and so forth like
this:-
What is the name of the student? abebe
Do you know the father's name of 'abebe' ? y/n y
What is the name of the father of 'abebe' ? kebede
Do you know the father's name of 'kebede' ? y/n y
What is the name of the father of 'kebede' ? alemu
Do you know the father's name of 'alemu' ? y/n h
Do you know the father's name of 'alemu' ? y/n j
Do you know the father's name of 'alemu' ? y/n n
The student's full name is * abebe kebede alemu *
any more students ? y/n y
what is the name of the student? alemitu
Do you know the father's name of 'alemitu' ? y/n y
what is the name of the father of 'alemitu' ? abebe
Do you know the father's name of 'abebe' ? y/n n
The student's full name is * alemitu abebe *
any more students ? y/n n
"""



while True:
    name = input("What is the name of the student? ")
    full_name = f"{name} "
    last_answer = name
    while True:
        choice = input(f"Do you know the father of '{last_answer}'? (y/n) ")
        if choice.lower() == 'n':
            print(f"The student's full name is {full_name}")
            break
        elif choice.lower() == 'y':
            father = input(f"What is the name of the father of '{last_answer}'? ")
            last_answer = father
            full_name += f"{father} "
        else:
            continue
    more = input("Any more students? (y/n) ")
    if more.lower() == 'y':
        continue
    else:
        break