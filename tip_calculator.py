print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 5 , 10 or 15 ? "))

people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)
print(bill_with_tip) 
print(f"total amount: {bill_with_tip}")
bill_per_person = bill_with_tip / people

print(bill_per_person)

print(f"per person:  {bill_per_person}")

total_amount = round(bill_with_tip , 2)
print(f"total amount: ${total_amount}")

final_amount = round(bill_per_person , 2)
print(f"Each person should pay: ${final_amount}")