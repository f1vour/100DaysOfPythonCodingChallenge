print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroad. where do you want to go?") #backslash can be used \
user = input("Type 'left' or 'right'\n") #.lower() function can be used to turn any string into all lower case

if user == "left" or user == "Left" or user == "LEFT":
    print("you've come to a lake. there is an island in the middle")

    user_1 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    if user_1 == "wait" or user_1 == "Wait" or user_1 == "WAIT":
        print("You arrived at the island unharmed. There is a house with 3 doors.")

        user_2 = input(" one red, one yellow, one blue. which do you choose?\n ")
        if user_2 == "yellow" or user_2 == "YELLOW" or user_2 == "Yellow":
            print("Hurray, You win.")
        elif user_2 == "red" or user_2 == "Red":
            print("you got burnt by fire. Game Over")
        elif user_2 == "blue" or user_2 == "Blue":
            print("Eaten by beasts. Game over")
        else:
            print("Game over")
    else:
        print("You got eaten by a shark. Game Over")

else:
    print("you fell into a hole. Game over.")



