from random import randint

num_of_dices = int(input("How many dice are we rolling? "))
num_of_sides = int(input("How many sides on each die? "))

def roll_dice():
    print('|', end = '')
    for dice in range(num_of_dices):
        side = randint(1,num_of_sides)
        print(f"{side}|", end ='')
    print()

roll_dice()

while input("Roll again? ('q' to quit) ") != 'q':
    roll_dice()
