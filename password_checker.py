import re

# Function to check password strength
def check_password_strength(password):
    # Initialize a list to hold the strength messages
    strength_messages = []

    # Check password length
    if len(password) < 8:
        strength_messages.append("Password is too short. It should be at least 8 characters.")
    else:
        strength_messages.append("Password length is good.")

    # Check for uppercase letter
    if not re.search("[A-Z]", password):
        strength_messages.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letter
    if not re.search("[a-z]", password):
        strength_messages.append("Password should contain at least one lowercase letter.")
    
    # Check for digits
    if not re.search("[0-9]", password):
        strength_messages.append("Password should contain at least one digit.")
    
    # Check for special characters
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength_messages.append("Password should contain at least one special character.")

    # Check for common passwords
    common_passwords = ['password', '123456', 'qwerty', 'abc123', 'letmein']
    if password.lower() in common_passwords:
        strength_messages.append("Password is too common and easy to guess.")

    # Print the results
    if len(strength_messages) == 1:
        print("Password is strong!")
    else:
        print("Password is weak due to the following reasons:")
        for message in strength_messages:
            print(message)

# Input password from user
password = input("Enter a password to check its strength: ")

# Check the password strength
check_password_strength(password)
