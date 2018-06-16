# Write a simple lottery drawing program. The lottery drawing should consist
# of six different numbers betweem 1 and 48.
from random import sample

def lottery_drawing():
    numbers = []
    for number in range(1, 49):
        numbers.append(number)
    return sample(numbers, 6)


print(lottery_drawing())
