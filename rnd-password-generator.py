from ast import While
import random

password = ""
rnd_range = []
while True:
    password_length = input("Please enter the desired length of your password (between 1 and 50 characters): ")
    try:
        password_length = int(password_length)
        if password_length in range(51):
            break
        else:
            print("Please enter a number between 1 and 50")
    except ValueError:
        print("You did not enter a valid number")

while True:
    print("Do you want your password to consist of....")
    if input("Uppercase letters? (Y/N) ").lower() == "y":
        rnd_range.append((65,90))
    if input("Lowercase letters? (Y/N) ").lower() == "y":
        rnd_range.append((97,122))
    if input("Digits? (Y/N) ").lower() == "y":
        rnd_range.append((48,57))
    if input("Special characters? (Y/N) ").lower() == "y":
        rnd_range.append((33,47))
    if rnd_range != []:
        break
    print("Your password cannot consist of nothing, let's try that again...")

for i in range(password_length):
    random_integer = random.randint(*random.choice(rnd_range))
    password += chr(random_integer)

print(password)