""" Use a list comprehensions to produce a list that consists of all palindromic
numbers between 100 and 1000. """

def palindromic_nums():
    return [num for num in range(100, 1001) if str(num) == str(num)[::-1]]

print(palindromic_nums())
