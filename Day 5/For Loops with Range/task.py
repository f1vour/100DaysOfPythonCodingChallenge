# Range function has to be used with the For Function

# for number in range(1, 11, 2):
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)



# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Create a loop with For and Range to go from 1 to 100.
for number in range(1, 101):
    # First check if the number is divisible by both 3 and 5.
    if number % 3 == 0 and number % 5 == 0: #this % modulo operator is used to check if a value can divide another number completely with no remainder
        print("FizzBuzz")

    # Then check if the number is only divisible by 3
    elif number % 3 == 0:
        print("Fizz")

    # Finally check if the number is only divisible by 5
    elif number % 5 == 0:
        print("Buzz")

    # If it's not divisible by either of those numbers, just print the number
    else:
        print(number)
