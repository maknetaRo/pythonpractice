""" Let L=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]. Use a list
comprehension to produce a list of the gaps between consecutive entries in L.
Then find the maximum gap size and the percentage of gaps that have size 2. """

L=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
differences = [L[i+1] - L[i] for i in range(len(L) - 1)]

print(differences)
max_number = max(differences)
count = 0
for num in differences:
    if num == 2:
        count += 1

percentage = round(count / len(differences) * 100, 2)

print("The maximum gap size is {} and the percentage of 2 is {}.".format(max_number, percentage))
