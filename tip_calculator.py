print("Welcome to the Tip Calculator.🧮")
total_bill = float(input(f"What is the total bill 💷? £"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 , or 15? "))
people_split_bill = int(input("How many people to split the bill 🧑‍🤝‍🧑 ? "))
total_bill_after_tip= ((total_bill*percentage_tip/100)+total_bill)/people_split_bill
round_off = (round(total_bill_after_tip,2))
print(f"Each person should pay💷: £{round_off}")