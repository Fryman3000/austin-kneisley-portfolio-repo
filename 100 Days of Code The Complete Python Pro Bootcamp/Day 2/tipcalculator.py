#Day 2 Project Tip Calculator


#tip calculate that can calculate the bill, tip, and even split for multiple people
print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
each_pay = total_bill / people

message = f'Each person should pay: ${each_pay:.2f}'
print(message)