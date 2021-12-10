#!/usr/bin/env python3

import random
from vars import rock
from vars import paper
from vars import scissors

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))


if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, disqualified!")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print(f"The computer chose:")
  print(game_images[computer_choice])

  if user_choice == computer_choice:
    print("Draw! Go again.")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose...")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice > user_choice:
    print("You lose!")
  else:
    print("You lose...")