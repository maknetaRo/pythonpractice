""" Ask the user to enter a list conataining numbers between 1 and 12. Then
replace all of the entries in the list that are greater than 10 with 10. """

items = input("Enter a list of numbers between 1 and 12 separated by comma: ")

print(items)

new_list = [10 if int(num) > 10 else int(num) for num in items.split(', ')]
print(new_list)
