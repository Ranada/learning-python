print("****Welcome to the toothpick game*****")
print("We start with 13 toothpicks.")
print("Take turns taking 1, 2, or 3 toothpicks.")
print("The player to take the last toothpick wins.\n")

player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")
current_player = player2
toothpicks = 13

def print_toothpicks():
    print()
    for i in range(toothpicks):
        print('|', end='')
    print()

while toothpicks > 0:
    print_toothpicks()

    if current_player == player2:
        current_player = player1
    else:
        current_player = player2

    choice = int(input(f"How many do you take, {current_player}? "))
    while choice != 1 and choice != 2 and choice != 3:
        print("You can only remove 1, 2, or 3 tootpicks. Try again.")
        choice = int(input(f"How many do you take, {current_player}? "))

    toothpicks -= choice
    if toothpicks > 0:
        print("There are " + str(toothpicks) + " left.")
    else:
        print(current_player, "won!\n")

print("*****Game Over*****")