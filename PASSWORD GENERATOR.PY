##### PASSWORD GENERATOR #######

import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters  # A-Z and a-z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # Special characters like !, @, #

    # Combine all character sets into one
    all_characters = letters + digits + symbols

    # Generate a password by randomly choosing characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# User input for password length
try:
    length = int(input("Enter the desired length of the password: "))
    if length < 4:  # Ensure that the password is reasonably complex
        print("Password length should be at least 4.")
    else:
        generated_password = generate_password(length)
        print("Generated Password:", generated_password)
except ValueError:
    print("Please enter a valid number.")


###How the code works:

###Character Sets:

###string.ascii_letters contains both uppercase and lowercase letters.
####string.digits contains numbers from 0 to 9.
####string.punctuation contains special characters like !, @, etc.
### Generating Password:

###A random character is selected from the combined character set for the length specified by the user.
###Input Validation:

###The code ensures the user enters a valid number and that the password length is at least 4 (for complexity).
  ##Example Usage:
##EXAMPLE:If you input 10 as the desired length, the program might output something like T@r7a9Z8!W.





