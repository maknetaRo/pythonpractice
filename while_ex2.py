"""
A good program will make sure that the data its users enter is valid. Write
a program that asks the user for a weight and converts it from kilograms to
pounds. Whenever the user enters a weight below 0, the program should tell them
that their entry is invalid and then ask them again to enter a weight.
"""
kilo = eval(input("Enter weight in kilograms: "))

while kilo < 0:
    kilo = eval(input("Your entry is invalid. Try again: "))

pounds = kilo * 2.20462262
print("{} kilograms is equal to {} pounds.".format(kilo, round(pounds, 2)))
