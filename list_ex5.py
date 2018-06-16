# Write a simple quote-of-the-day program. The program should contain a list of
# quotes, and when the user runs the program, a randomlly selected quote should
# be printed.
from random import choice

def quote_of_the_day(list_of_quotes):

    return choice(list_of_quotes)

list_of_quotes = [
        'A friend in need is a friend indeed.',
        'Better late than never.',
        'Love is blind.',
        'Where there is a will, there is a way.',
        'An apple a day keeps the doctor away.',
        'Easy come, easy go.',
        'East or west, home is best.',
        'Easy come, easy go.',
        'Time is money.',
        'Easier said than done.',
        'All is well that ends well.'
        'An eye for an eye, and a tooth for a tooth.',
        'Blood is thicker than water.',
        'A friend to all is a friend to none.',
        'Beware of a silent dog and still water.',
        'A liar will not be believed, even when he speaks the truth.',
        'Every man has his faults.',
        'Never judge a book by its cover.',
        'A  sound mind in a sound body.',
        'A change is as good as a rest.',
        'A man is as old as he feels.',
        'Experience is the mother of wisdom.',
        ]

print(quote_of_the_day(list_of_quotes))
