# a. Ask the user to enter a sentence and print out the third word of the sentence

sentence = input("Enter a sentence: ")
sentence = sentence.split(' ')
print(sentence[2])

# b. Ask the user to enter a sentence and print out every third word of the sentence
print(sentence[0::3])
