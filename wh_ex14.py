"""
Write a program to play the following simple game. The player starts
with $100. On each turn a coin is flipped and the player has to guess
heads or tails. The player wins $9 for each correct guess and loses
$10 for each incorrect guess. The game ends either when the player
runs out of money or gets to $200.
"""
import random
total = 100

while total > 0 and total < 200:
    player_choice = int(input("Enter 1 for heads and 0 for tails: "))
    if player_choice == random.randint(0,1):
        total += 9
        print("Your total is {}.".format(total))
    else:
        total -= 10
        print("Your total is {}.".format(total))
