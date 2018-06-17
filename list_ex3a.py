""" Start with the list [8, 9, 10]. Do the following: """

L = [8, 9, 10]

# a. Set the second entry (index) to 17
L[1] = 17
print(L)
# b. Add 4, 5, and 6 to the end of the list
L = L + [4, 5, 6]
print(L)
# c. Remove the first entry from the list
L.remove(8)
print(L)
# d. Sort the list
L.sort()
print(L)
# e. Double the list
L = L * 2
print(L)
# f. Insert 25 at index 3
L.insert(3, 25)
print(L)

# The final list should equal [4, 5, 6, 25, 10, 17, 4, 5, 6, 10, 17]
