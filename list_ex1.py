# write a progrma that asks user to enter some text and then counts how many
# articles are in the textself.

def count_articles(text):
    """Return the number of articles (a, an, the) in the text"""
    list_of_words = text.split(' ')
    list_of_articles = []
    for element in list_of_words:
        if element.strip(',') == 'a' or element.strip(',') == 'an' or element.strip(',') == 'the':
            list_of_articles.append(element)
    print(list_of_articles)
    return len(list_of_articles)


text = input("Enter a text: ")
print(count_articles(text))
