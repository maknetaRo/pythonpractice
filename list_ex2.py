# Write a program that allows the user to enter five numbers (read as strings).
# Create a string that consists of the user's numbers separated by plus signs.


def five_numbers(numbers):
   
    return '+'.join(numbers.split(', '))

numbers = input("Enter five numbers separted by comma: ")
print(five_numbers(numbers))
