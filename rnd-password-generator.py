import random

password = ""
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
for i in range(password_length):
    random_integer = random.randint(48, 122)
    password += chr(random_integer)

print(password, len(password))