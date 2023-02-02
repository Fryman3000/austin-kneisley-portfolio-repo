#Leap Year

#program that works out whether if a given year is a leap year
year = int(input("Which year do you want to check? "))

if year % 100 == 0:
    if year % 400 == 0:
        print("Leap year.")
elif year % 4 == 0:
        print("Leap year.")
else:
    print("Not leap year.")