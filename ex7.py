"""
Recall that, given a string s , s.index( ' x ' ) returns the index of the
first x in s and an error
if there is no x.
(a) Write a program that asks the user for a string and a letter. Using
a while loop, the
program should print the index of the first occurrence of that letter
and a message if the
string does not contain the letter.
"""
sentence = input("Enter a string: ")
letter = input("Enter a letter: ")

index = 0
while index < len(sentence)-1:
    index += 1
if letter in sentence:
    print(sentence.index(letter))
else:
    print("String does not contain letter {}.".format(letter))


"""
(b) Write the above program using a for/break loop instead of a while loop.
"""
sentence = input("Enter a string: ")
letter = input("Enter a letter: ")

for index in range(len(sentence)):
    if letter in sentence:
        print(sentence.index(letter))
        break

    else:
        print("String does not contain letter {}.".format(letter))
        break
