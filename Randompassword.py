import random
import string

def generate_random_password(length=12):
    # Define a set of characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use a loop to generate random characters and build the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Return the generated password
    return password

# Ask the user for the desired password length
password_length = int(input("Enter the length of the password: "))

# Generate a random password using the specified length
random_password = generate_random_password(password_length)

# Display the generated password
print("Random Password:", random_password)
