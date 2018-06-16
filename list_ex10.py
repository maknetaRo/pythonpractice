""" Write a censoring program. Allow the user to enter some text and your
program should print out the text with all the curse words starred out. The
number of stars should match the length of the curse word. For the purposes of
this program, just use the 'curse' words darn, dang, freakin, heck and shoot.
Sample output is below."""

text = input("Enter a text: ")
curse = ['darn', 'dang', 'freakin', 'heck', 'shoot']

text = text.split(' ')
new_text = []
for elem in text:
    elem = elem.strip(',')
    if elem in curse:
        new_text.append(elem.replace(elem, '*' * len(elem)))
    elif elem not in curse:
        new_text.append(elem)

print(' '.join(new_text))
