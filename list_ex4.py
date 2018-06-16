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
