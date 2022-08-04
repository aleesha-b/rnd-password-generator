import random

password = ""
for i in range(10):
    random_integer = random.randint(0, 126)
    password += chr(random_integer)

print(password, len(password))