"""
Write a program that counts how many of the squares of the numbers from
1 t0 100 end in 1.
"""
count = 0
for num in range(1, 101):
    if str(num ** 2)[-1] == "1":
        print("The square of {} is {}.".format(num,str(num**2)))
        count += 1

print("There are {} squares of the numbers end in 1.".format(count))
