"""
Write a program that counts how many of the squares of the numbers
form 1 to 100 end in a 4 and how many end in a 9.
"""

count4 = 0
count9 = 0

for num in range(1, 101):
    if str(num**2)[-1] == "4":
        print("The square of {} is {}.".format(num,str(num**2)))
        count4 += 1
    elif str(num**2)[-1] == "9":
        print("The square of {} is {}.".format(num,str(num**2)))
        count9 +=1

print("There are {} numbers end in 4 and {} numbers end in 9.".format(count4, count9))
