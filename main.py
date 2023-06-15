import random

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

# Write your code below this line 👇
choices = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors game!\n")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
random_choice = random.randint(0, 2)

print("PLAYER: ")
print(choices[user_choice])
print("COMPUTER: ")
print(choices[random_choice])

if(user_choice == random_choice):
    print("DRAW")
elif(user_choice == 0 and random_choice == 1 or user_choice == 1 and random_choice == 2 or user_choice == 2 and random_choice == 0):
    print("Computer Wins")
else:
    print("Player Wins")


