# a. Write a program that asks the user to enter a sentence and then randomly
# rearranges the words of the sentence. Don't worry about getting punctuation
# or capitalization correct.
from random import shuffle

def random_sentence(sentence):
    """Return randomly rearranged words in a sentece"""
    sentence_into_list = sentence.split(' ')
    shuffle(sentence_into_list)
    new_sentence = []
    for element in sentence_into_list:
        new_sentence.append(element)
    return ' '.join(new_sentence)

sentence = input("Write a sentence: ")
print(random_sentence(sentence))

# b. Do the above problem, but now make sure that the sentence starts with a
# capital, that the original first word is not capitalized if it comes in the
# middle of the sentence, and that the period is in the right place.

def random_sentence(sentence):
    """Return randomly rearranged words in a sentece"""
    sentence_into_list = sentence.split(' ')
    shuffle(sentence_into_list)
    new_sentence = []
    for element in sentence_into_list:
        new_sentence.append(element.strip('.').lower())
    return ' '.join(new_sentence).capitalize()

sentence = input("Write a sentence: ")
print(random_sentence(sentence))
