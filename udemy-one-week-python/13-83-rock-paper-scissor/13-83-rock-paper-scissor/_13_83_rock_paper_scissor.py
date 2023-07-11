from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
def getComputerMove(num):
    if num == 1: return rock
    if num == 2: return paper
    if num == 3: return scissors

computer_move = getComputerMove(num)


# Ask a user to enter their move
user_entry = input("What is your move? ").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
def getUserMove(user_entry):
    if user_entry == "rock": return rock
    if user_entry == "paper": return paper
    if user_entry == "scissors": return scissors

user_move = getUserMove(user_entry)

print("Your move:")
print(user_move)
print()

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("Computer's move:")
print(computer_move)
print()


# Figure out who wins and print the result!
if user_move == computer_move: print("Draw!")

if user_move == rock:
    if computer_move == paper: print("Computer wins!")
    if computer_move == scissors: print("You win!")

if user_move == paper:
    if computer_move == rock: print("You win!")
    if computer_move == scissors: print("Computer wins!")

if user_move == scissors:
    if computer_move == rock: print("Computer wins!")
    if computer_move == paper: print("You win!")
