import random
import string
import time

length = int(input("Enter the password length: "))

capital_char = string.ascii_uppercase
small_char = string.ascii_lowercase
digits = string.digits
special_char = string.punctuation

# Creating a list of all Characters
char = []
char.extend(list(capital_char))
char.extend(list(small_char))
char.extend(list(digits))
char.extend(list(special_char))

# Using For-Loop to generate 3 passwords for the User
for i in range(1, 4):
    # Shuffling all the Characters
    random.shuffle(char)
    password = ''.join(char[:length])
    # Delaying response by 1 sec 
    time.sleep(1)
    print(f"Pasword # {i}: {password}")
