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

game_images = [rock, paper, scissors]
user_choice = int(input("what do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n" ))
if user_choice >= 0 and user_choice <= 2 :
   print(f"user chose: {game_images[user_choice]}") #why the list didn't append the user_choice  variable is because it is an int, and it is outputting what is inside the list
# else:
#     print("You inputted the wrong number, you loose")

computer_choice =  random.randint(0,2)
print(f"computer chose: {game_images[computer_choice]}")


if user_choice == 0 and computer_choice == 2:
    print("you win")
if user_choice >=3 or user_choice < 0:
    print("You inputted the wrong number, you loose")
elif computer_choice == 0 and user_choice == 2:
    print("you loose")
elif computer_choice > user_choice:
    print("you loose")
elif user_choice > computer_choice:
    print("you win")
elif user_choice == user_choice:
    print("its a draw!")

