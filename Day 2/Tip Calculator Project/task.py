print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n $"))
tip = int(input("What percentage tip would you like to give? 10% 12% 15% \n"))
people = int(input("How many people to split the bill? \n"))

bill_with_tip = bill * (tip/100) + bill #the percentage tip to give from the amount of bill
#print(bill_with_tip)
total_bill = bill_with_tip / people
final_amount = round(total_bill, 2)
print(f"Each person should pay : ${final_amount}")



