# Mind Map:  Print the table - Modify the table - Check the status (check for win - check for draw)
# A little buggy but it works
from os import system
from random import choice as rand


table = ([
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
])
values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
status = 0
wins = [
        ( (0,0), (0,1), (0,2) ), # Horizontal one
        ( (1,0), (1,1), (1,2) ), # Horizontal Two
        ( (2,0), (2,1), (2,2) ), # Horizontal Three
        
        ( (0,0), (1,0), (2,0) ), # Vertival one
        ( (0,1), (1,1), (2,1) ), # Vertical Two
        ( (0,2), (1,2), (2,2) ), # Vertical Three

        ( (0,0), (1,1), (2,2) ), # Diagonal one
        ( (0,2), (1,1), (2,0) ), # Diagonal Two
    ]

def print_table():
    """0974994420"""
    system("cls")
    for row in table:
        for element in row:
            print(f"| {element} |", end=" ")
        print("")

def modify_table(no, val):
    """Modify"""
    if no < 4:
        ex = no - 1
        ind = 0
    elif no < 7:
        ex = no - 4
        ind = 1
    elif no < 10:
        ex = no - 7
        ind = 2
    else:
        ind = None

    if ind is not None:
        if table[ind][ex] in values:
            table[ind][ex] = val
            return True
    return False

def is_win():
    """Checks the win status"""
    for awin in wins:
        if table[awin[0][0]][awin[0][1]] == table[awin[1][0]][awin[1][1]] == table[awin[2][0]][awin[2][1]]:
            return table[awin[0][0]][awin[0][1]]
    return False

def is_draw():
    """_summary_
    """
    for row in table:
        for val in row:
            if val in values:
                return False
    return True
def final_move():
    """_summary_
    """
    for awin in wins:
        if (table[awin[0][0]][awin[0][1]] == table[awin[1][0]][awin[1][1]] == "O") and table[awin[2][0]][awin[2][1]] in values:
            return table[awin[2][0]][awin[2][1]]
        elif (table[awin[0][0]][awin[0][1]] == table[awin[2][0]][awin[2][1]] == "O") and table[awin[1][0]][awin[1][1]]in values:
            return table[awin[1][0]][awin[1][1]]
        elif (table[awin[2][0]][awin[2][1]] == table[awin[1][0]][awin[1][1]] == "O") and table[awin[0][0]][awin[0][1]] in values:
            return table[awin[0][0]][awin[0][1]]
    for awin in wins:
        if (table[awin[0][0]][awin[0][1]] == table[awin[1][0]][awin[1][1]] == "X") and table[awin[2][0]][awin[2][1]] in values:
            return table[awin[2][0]][awin[2][1]]
        elif (table[awin[0][0]][awin[0][1]] == table[awin[2][0]][awin[2][1]] == "X") and table[awin[1][0]][awin[1][1]] in values:
            return table[awin[1][0]][awin[1][1]]
        elif (table[awin[2][0]][awin[2][1]] == table[awin[1][0]][awin[1][1]] == "X") and table[awin[0][0]][awin[0][1]] in values:
            return table[awin[0][0]][awin[0][1]]
    return False

def computer_move():
    """
    Computer is "O"
    """
    avaliable_moves = []
    corner_moves = ["1", "3", "7", "9"]
    avail_cm = []
    for row in table:
        for val in row:
            if val in values:
                if val in corner_moves:
                    avail_cm.append(val)
                avaliable_moves.append(val)
    if final_move():
        return final_move()
    elif "5" in avaliable_moves:
        return "5"
    elif len(avail_cm) > 0:
        return rand(avail_cm)
    else:
        return rand(avaliable_moves)


def check_status():
    """check status"""
    global status
    if is_win() is not False:
        status = f"Player {is_win()} won!"
    elif is_draw():
        status = f"The Game is Draw!"
    else:
        status = 0

system("cls")
print("Welcome to X-O Game")
player = input("1) One Player \n2) Two player\n Your choice(1/2):  ")
one = False
if player == "1":
    input("ONE PLAYER MODE...\nPress any key to continue")
    one = True

while status == 0:
    print_table()
    ch1 = int(input("Player 1: "))
    cx = modify_table(ch1, "X")
    while cx is False and status == 0:
        print_table()
        ch1 = int(input("Invalid choice. Player 1: "))
        cx = modify_table(ch1, "X")
    print_table()
    check_status()
    if status != 0:
        break
# Player 2's Turn
    if not one:
        ch2 = int(input("Player 2: "))
    else:
        ch2 = int(computer_move())
    co = modify_table(ch2, "O")
    while co is False and status == 0:
        print_table()
        ch2 = int(input("Invalid choice. Player 2: "))
        co = modify_table(ch2, "O")
    check_status()
    if status != 0:
        break

if status != 0:
    print_table()
    print(f"Game finished. The result is {status}")
