""" Write a program that generates a list of 20 random numbers between 1 and 100.
"""
from random import sample
# a. Print the list.
list_of_nums = [num for num in range(1, 101)]
list_of_nums = sample(list_of_nums, 20)
print(list_of_nums)
# b. Print the average of the elements in the list.
average = sum(list_of_nums)/ len(list_of_nums)
print("The average of the list is {}".format(average))
# c. Print the largest and smallest values in the list.
print("The largest number is {}.".format(max(list_of_nums)))
print("The smallest value is {}.".format(min(list_of_nums)))
# d. Print the second largest and second smallest entries in the list.
list_of_nums.sort()
print("The second largest number is {} and the second smallest entry is {}".format(list_of_nums[-2], list_of_nums[1]))
# e. print how many even numbers are in the list.
even_nums = [num for num in list_of_nums if num % 2 == 0]

print("The number of even elements in the list is {}.".format(len(even_nums)))
