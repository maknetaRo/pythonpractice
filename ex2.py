"""
(a) Write a program that uses a while loop (not a for loop) to read through
 a string and print
the characters of the string one-by-one on separate lines.
"""
strng = input("Enter a string: ")
i = 0
while i < len(strng):
    print(strng[i])
    i += 1

"""
(b) Modify the program above to print out every second character of the
 string.
 """
strng = input("Enter a string: ")
i = 0
while i < len(strng):
    print(strng[i])
    i += 2
