"""
workflow of project
1. input from user (rock, paper, scissor)
2. computer choice(using random function)
3. Result print

Cases:
A - Rock
Rock - Rock = tie
Rock - paper = Paper wins
Rock - scissor = rock wins

B - Paper
Paper - Paer = tie
Paper - Rock = Paper wins
Paper - scissor = sciccor wins

C - Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock wins
Scissor - Paper = Scissor wins

"""

import random

choices = ["rock", "paper", "scissor"]

user_choice = input("Enter your move: rock/paper/scissor ")
comp_choice = random.choice(choices)

print(f"user choice = {user_choice} & computer choice = {comp_choice}")

if user_choice == comp_choice :
    print("Tie")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("Comp wins")
    else:
        print("user wins")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("Comp wins")
    else:
        print("user wins")

elif user_choice == "scissor":
    if comp_choice  == "rock":
        print("comp wins")
    else:
        print("user wins")

