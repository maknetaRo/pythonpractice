"""
5. Write a program that asks the user to enter a number and prints the sum
 of the divisors of
that number. The sum of the divisors of a number is an important function
in number theory.
"""
number = int(input("Enter a number: "))

total = 0
for num in range(1, number+1):
    if number % num == 0:
        
        total += num

print("The sum of all divisors of {} equals {}.".format(number, total))
