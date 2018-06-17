""" Create the following lists using a for loop. """
# a. A list consisting of the integers 0 through 49.
L = [num for num in range(0, 50)]
print(L)

# b. A list containing the squares of the integers 1 through 50.
L = [num ** 2 for num in range(1, 51)]
print(L)

# c. the list ['a', 'bb', 'ccc', 'dddd', ...] that ands with 26 copies of the
# letter z.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
L = []
num = 1
for char in alphabet:
    L.append(char * num)
    num += 1

print(L)
