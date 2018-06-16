""" Write a simple quiz game that has a list of the questions and a list of
answers to those questions. The game should give the player four randomly selected
questions to answer. It should ask the questions one by one, and tell the
player whether they got the question right or wrong. At the end it should
print out how many out of four they got right."""

from random import sample

def simple_quiz(questions, answers):
    count = 0
    for question in sample(questions, 4):
        print(question)
        answer = input("> ").title()
        if answer.title() not in answers:
            continue
        if answers.index(answer) == questions.index(question):
            count += 1

    return "You gave {} correct answers.".format(count)



questions = [
"What is the capital city of Poland?",
"How much is 25 divided by 5?",
"What is the square root of 4?",
"Which is the nearest star to planet earth?",
"Which is the fastest animal on the land?",
"Which is the longest river on the earth?",
"How much is Pi number?",
"What is the currency of Japan?",
" What country has a maple leaf on their national flag?"
]
answers = ["Warsaw", "5", "2", "Sun", "Cheeta", "Nile", "3.14", "Yen", "Canada"]

print(simple_quiz(questions, answers))
