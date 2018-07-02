"""
Write a program that has a list of ten words, some of which have
repeated letters and some which don’t. Write a program that picks
a random word from the list that does not have any
repeated letters.
"""
from random import choice

lst = ['read', 'book', 'grade', 'bring', 'except', 'egg', 'room', 'true',
'mate', 'cup']
new_lst = []
i = 0
while i < len(lst):

    if len(lst[i]) == len(set(lst[i])):
        new_lst.append(lst[i])
    i += 1
print(choice(new_lst))
