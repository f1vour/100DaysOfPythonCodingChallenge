# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S, M or L: ")
#Mine work, I got the answer but the code is still too long and takes too uch computer resources
# if size == "S":
#     bill = 15
#     print("Your bill for size S is $15")
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#     if pepperoni == "Y":
#         bill += 2
#         print(f"Plus pepperoni is ${bill}")
#
#     extra_cheese = input("Do you want extra cheese? Y or N: ")
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your final bill is ${bill}")
#
# elif size == "M":
#     bill = 20
#     print("Your bill for size M is $20")
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#     if pepperoni == "Y":
#         bill += 3
#         print(f"Plus pepperoni is ${bill}")
#
#     extra_cheese = input("Do you want extra cheese? Y or N: ")
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your final bill is ${bill}")
#
#
# elif size == "L":
#     bill = 25
#     print("Your bill for size L is $25")
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#     if pepperoni == "Y":
#         bill += 3
#         print(f"Plus pepperoni is ${bill}")
#
#     extra_cheese = input("Do you want extra cheese? Y or N: ")
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your final bill is ${bill}")
#
#
# else:
#     print("Your typed the wrong input")


#Try sth different
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S, M or L: ")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size =="L":
#     bill += 25
# else:
#     print("You typed the wrong input.")
#
# # Add their bill based on pepperoni choice
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# if pepperoni == "Y":
#     if size == "S":
#        bill += 2
#     else:
#        bill += 3
#
# # Add based on cheese choice
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")


#Bank App

amount = 10000
print("Welcome to Kandi Bank ")
user = input("Do you want to withdraw or deposit? ")

if user == "withdraw" or user == "w":
    print(f"you have this amount {amount} in your account")
elif user == "deposit" or user == "d":
    print("How much do you want to deposit? ")
else:
    print("You pressed the wrong input")

value = int(input("How much do you want to withdraw?"))
if value <= 5000 or value >= 5000:
    amount -= value
else:
    print("You have exceeded the withdrawal limit")

print(f"Withdrawal successful, you have this amount left: {amount}")