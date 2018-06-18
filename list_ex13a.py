""" Write a program that removes an repeated items from a list so that each item
appears at most once. Don't use set() """

L = [1, 2, 3, 2, 3, 1, 2, 3, 4, 5, 0, 0, 1, 7, 8]

for elem in L:
    if elem not in new_list:
        new_list.append(elem)

print(new_list)
