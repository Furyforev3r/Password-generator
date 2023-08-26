import random # import random module
import string # import string module

def Generator():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars # concatenate the letters, digits and special_chars

    print("Welcome to the password generator!")
    pwd_length = int(input("How long do you want your password to be? ")) # get the length of the password

    pwd = ''.join(random.choice(alphabet) for i in range(pwd_length)) # generate a random password

    print(f"Your password is: {pwd}") # print the password
    restart = input("Would you like to generate another password? (y/n) ") # ask if the user wants to generate another password
    if restart == "y": # if the user wants to generate another password
        Generator() # call the function again
    else: # if the user doesn't want to generate another password
        print("Goodbye!") # print goodbye

if __name__ == "__main__":
    Generator() # call the function
