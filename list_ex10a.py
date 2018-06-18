""" Write a program that rotates the elements of a list so that the
 element at the first index moves to the second index, the element in
 the second index moves to the third index, etc., and the element in the last
 index moves to the first index. """

L = ["Ala", "Ola", "Ela", "Basia", "Krysia", "Zosia"]
new_list = []
for i in range(len(L)):
    new_list.append(L[i-1])

print(new_list)
