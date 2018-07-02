"""
The GCD (greatest common divisor) of two numbers is the largest number
that both are divisible by. For instance, gcd (18, 42) is 6 because
the largest number that both 18 and 42 are divisible by is 6. Write a
program that asks the user for two numbers and computes their gcd.
Shown below is a way to compute the GCD, called Euclid’s Algorithm.
• First compute the remainder of dividing the larger number by the smaller
 number
• Next, replace the larger number with the smaller number and the smaller
 number with the remainder.
• Repeat this process until the smaller number is 0. The GCD is the last
value of the larger number.
"""
def gcd(n1, n2):
    if n1 > n2:
        for n in range(1, n1):
            remainder = n1 % n2
            n1, n2 = n2, remainder
            if remainder == 0:
                break
        return n1
    elif n2 > n1:
        for n in range(1, n2):
            remainder = n2 % n1
            n2, n1 = n1, remainder
            if remainder == 0:
                break
        return n2

if __name__ == "__main__":
    n1 = int(input("Enter a first number: "))
    n2 = int(input("Enter a second number: "))
    print(gcd(n1, n2))

# short and sweet but not mine
def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

if __name__ == "__main__":
    print(gcd(56, 64))
