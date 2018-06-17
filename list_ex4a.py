""" Ask the user to enter a list of strings. Create a new list that consists
 of those strings with their first character removed."""
 
list_of_strings = input("Enter a list of strings separated by comma: ")
new_strings = [elem[1:] for elem in list_of_strings.split(', ')]
print(new_strings)
