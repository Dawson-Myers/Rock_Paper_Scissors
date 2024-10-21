rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rps_choices = [rock, paper, scissors]

user_choice = input("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")

if user_choice == '0':
    print(rock)
if user_choice == '1':
    print(paper)
if user_choice == '2':
    print(scissors)

random_index = random.randint(0, 2)
computer_choice = rps_choices[random_index]

# print(random_index)

print("Computer chose:")
print(computer_choice)

if random_index == int(user_choice):
    print("It's a draw!")
if random_index == 0 and user_choice == '1':
    print("You Win!")
if random_index == 1 and user_choice == '2':
    print("You Win!")
if random_index == 2 and user_choice == '0':
    print("You Win!")
if random_index == 2 and user_choice == '1':
    print("You Lose!")
if random_index == 1 and user_choice == '0':
    print("You Lose!")
if random_index == 0 and user_choice == '2':
    print("You Lose!")


