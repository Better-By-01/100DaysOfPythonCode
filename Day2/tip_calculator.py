print("Welcome to the tip calculator.")
bill = float(input("What was the bill bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

per_person = (bill + (tip/100)*bill)/(people)
#print(f"Each person should pay: ${round(per_person, 2)}")

# OR
final_amount = "{:.2f}".format(per_person)
print(f"Each person should pay: ${final_amount}")