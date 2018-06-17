""" Let L be a list of strings. Write list comprehensions that create new lists
 form L for each of the following"""

 #A list that consists of the strings of s with their first characters removedself.

L = ['mother', 'father', 'sister', 'brother', 'uncle', 'aunt', 'cousin', 'me']

new_list = [elem[1:] for elem in L]
print(new_list)

# A list of the lengths of the strings of s

length_list = [len(elem) for elem in L]
print(length_list)

# A list that consists of only those strings of s that are at least three
# characters long.

three_char = [elem for elem in L if len(elem) >= 3]
print(three_char)
