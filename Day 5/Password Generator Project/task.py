import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = 4
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# Easy Level
# password = ""
#
# # Creating a loop where the user can be able to generate 4 characters or more
# # 1 - 4 , nr_letters = 4
# for char in range(0, nr_letters):
#       # random_char =  random.choice(letters) # longer to write
#       # password += random_char
#       password += random.choice(letters)  #random.choice used to select characters randomly
#
# for num in range(1, nr_numbers + 1):
#       password += random.choice(numbers)
#
# for symbol in range(1, nr_symbols + 1):
#       password += random.choice(symbols)
#
# #print(password)


# Hard Level to shuffle the numbers, not to be printed out serially
password = ""
for char in range(0, nr_letters):
      password += random.choice(letters) #what is taking place here is concatenation of strings

for num in range(1, nr_numbers + 1):
      password += random.choice(numbers)

for symbol in range(1, nr_symbols + 1):
      password += random.choice(symbols)

# Convert the password into a list, why? because random.shuffle function only works on lists, not strings
password = list(password)

# Shuffled the list
random.shuffle(password)

# Change the list back into a string
new_password = "".join(password)
print(f"Your new password is: {new_password}")

# Another format
# password_list = []
# for char in range(0, nr_letters):
#       password_list.append(random.choice(letters))
# #       print(password_list)
# # print(password_list)
# for num in range(1, nr_numbers + 1):
#       password_list.append(random.choice(numbers))
#
# for symbol in range(1, nr_symbols + 1):
#       password_list.append(random.choice(symbols))
#
# random.shuffle(password_list)
#
# password =""
# for char in password_list:
#     password += char
#     print(password)
#
# print(f"Your password is: {password}")
#
