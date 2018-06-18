"""
Write a program that asks the user to enter a password. If the user enters the
right password, the program should tell them they are logged into the system.
Otherwise, the program should ask them to reenter the password. The user should
only get five tries to enter the password, after which point the program
should tell them that they are kicked off of the system.
"""
password = input("Enter a password: ")

logged = "1234ba"
tries = 1
while tries < 5:
    if password == logged:
        print("You are logged into the system.")
        break
    else:
        print("Reenter the password.")
        password = input("Enter a password: ")
        tries += 1

    print("After 5 tries, you are kicked off of the system.")
