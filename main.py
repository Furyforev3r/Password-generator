import random
import string

def Generator():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    print("Welcome to the password generator!")
    pwd_length = int(input("How long do you want your password to be? "))

    pwd = ''.join(random.choice(alphabet) for i in range(pwd_length))

    print(f"Your password is: {pwd}")
    restart = input("Would you like to generate another password? (y/n) ")
    if restart == "y":
        Generator()
    else:
        print("Goodbye!")
Generator()