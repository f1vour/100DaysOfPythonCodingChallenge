# Operators is a symbol in programing -
# Modulo performs the division and gives us the remainder of the division

print("Checking the number if its Odd or an Even number!")
number = int(input("Enter a number: "))
#denominator = int(input("Enter a denominator number: "))

check = number % 4
print(check)

if check == 0:
    print("Even")
else:
    print("Odd")


