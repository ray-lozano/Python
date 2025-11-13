# Day 2 python programming project tip calculator

# Print the greeting and ask the user various questions to
# determine how much to tip and how much each person should tip

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Calculate the tip and the bill and output that amount
each_pay = (bill / people) * (1 + tip/100)

print(f"Each person should pay: ${each_pay:.2f}")