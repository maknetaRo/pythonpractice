""" Write a program that asks the user for an integer and creates a list that
consists of the factors of that integer. """

def factors(number):
    return  [i for i in range(1, number + 1) if number % i == 0]


number = int(input("Enter a number: "))
print(factors(number))
