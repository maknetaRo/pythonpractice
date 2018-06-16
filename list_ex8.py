"""Write a program that simulates drawing names out of a hat. In this drawing,
the number of hat entries each person gets may vary. Allow the user to input
a list of names and a list of how many entries each person has in the drawing,
and print out who wins the drawing."""

from  random import sample

def hat_drawing(names, entries):
    names = names.split(', ')
    if len(names) >= entries:
        return sample(names, entries)
    else:
        return "The number of entries should be smaller than the number of names."


names = input('Enter a list of names: ')
entries = int(input("Enter a number: "))
print(hat_drawing(names, entries))
