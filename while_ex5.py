"""
Write a program that allows the user to enter any number of test scores. The user
indicates they are done by entering in a negative number. Print how many of the
scores are A's (90 or above). Also print out the average.
"""

print("Enter a test score.")
print("If you want to finish choose a negative number.")

score = 0
scores = []
grades = []
while score >= 0:
    print("Enter a test score.")
    score = int(input(">  "))
    scores.append(score)

for score in scores:
    if score > 90:
        grades.append("A")
    elif score > 75:
        grades.append("B")
    elif score > 60:
        grades.append("C")
    elif score > 50:
        grades.append("D")
    elif score > 40:
        grades.append("E")
    elif score > 0:
        grades.append("F")
    elif score < 0:
        scores.pop()


print(scores)
print(grades)

print("There are {} A's.".format(grades.count("A")))
print("There are {} B's.".format(grades.count("B")))
print("There are {} C's.".format(grades.count("C")))
print("There are {} D's.".format(grades.count("D")))
print("There are {} E's.".format(grades.count("E")))
print("There are {} F's.".format(grades.count("F")))
average = sum(scores) / len(scores)
average = round(average, 2)
print("Average test score is {}.".format(average))
