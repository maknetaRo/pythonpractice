"""Write a program that gets a string from the user containing a potential
telephone number. The program print Valid if it decides the phone number is a
real phone number, and Invalid otherwise. A phone number is consider valid
as long as it is written in the form abc-def-ijk or +48-abc-def-ijk. The dashes
must be included and the number of digits in each group must be correct."""

def valid_number(number):
    telephone_number = number.split('-')
    print(telephone_number)
    if len(telephone_number) == 3:
        for elem in telephone_number:
            if elem.isdigit:
                return "Valid"
            else:
                return "Invalid"
    elif len(telephone_number) == 4:
        for elem in telephone_number:
            if telephone_number[0] == '+48' and elem.isdigit:
                return "Valid"
            else:
                return "Invalid"


number = input("Enter a telephone number. Remember to divide groups of three with dashes.")
print(valid_number(number))
