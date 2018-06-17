""" Write a program that asks the user to enter a list of integers. Do the
following:"""

items = input("Enter a list of numbers divided with comma: ")
items = items.split(', ')
new_items = [int(item) for item in items]

# a. Print the total number of items in the list.
print(len(new_items))
# b. Print the last item in the list.
print(int(new_items[-1]))
# c. Print the list in reverse order.
print(new_items[::-1])
# d. Print Yes if the list contains a 5 and No otherwise.
if 5 in new_items:
    print("Yes")
# e. print the number of fives in the list.
count = 0
for item in new_items:
    if item == 5:
        count += 1
print("There are {} element(s) equal(s) 5 in the list.".format(count))
# f. Remove the first and last items from the list, sort the remaining items,
# and print the result.
new_list = new_items[1:-1]
print(sorted(new_list))
# g. Print how many integers in the list are less than 5.
count = 0
for num in sorted(new_list):
    if num < 5:
        count += 1
print("There are {} numbers lower than 5.".format(count))
