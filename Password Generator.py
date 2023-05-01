# Password Genreator with Python
import random
import string

# Define a function to generate a random password
def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by selecting characters from the character set
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Prompt the user to enter the desired length of the password
length = int(input("Enter the length of the password you want to generate: "))

# Generate the password and display it to the user
password = generate_password(length)
print("Your random password is:")
print(password)
