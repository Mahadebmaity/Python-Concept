# import random
# import pyperclip
# def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
#     """Generate a random password with the specified criteria."""
#     lowercase = 'abcdefghijklmnopqrstuvwxyz'
#     uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if use_uppercase else ''
#     numbers = '0123456789' if use_numbers else ''
#     special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?/' if use_special_chars else ''

#     all_characters = lowercase + uppercase + numbers + special_chars

#     if not all_characters:
#         raise ValueError("At least one character type must be selected.")

#     password = ''.join(random.choice(all_characters) for _ in range(length))
#     return password
# def copy_to_clipboard(password):
#     """Copy the generated password to the clipboard."""
#     pyperclip.copy(password)
#     print("Password copied to clipboard.")
# def main():
#     """Main function to run the password generator."""
#     try:
#         length = int(input("Enter password length (default 12): ") or 12)
#         use_uppercase = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
#         use_numbers = input("Include numbers? (y/n, default y): ").lower() != 'n'
#         use_special_chars = input("Include special characters? (y/n, default y): ").lower() != 'n'

#         password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
#         print(f"Generated Password: {password}")
#         copy_to_clipboard(password)

#     except ValueError as e:
#         print(f"Error: {e}")
# if __name__ == "__main__":
#     main()


# This code is a simple password generator that allows users to specify the length and character types of the password.
# It uses the `pyperclip` library to copy the generated password to the clipboard.
# Ensure you have the `pyperclip` library installed:
# pip install pyperclip
# The code includes error handling for invalid inputs and provides default values for the password generation parameters.
# The main function prompts the user for input and generates a password based on the specified criteria.
# The generated password is printed to the console and copied to the clipboard for easy access.
# The code is designed to be run as a standalone script.
# It can be easily modified to include additional features or customization options as needed.
# The password generation logic ensures that at least one character type is selected, raising an error if



# modified version of the original code 
''' 
import random
import pyperclip

def generate_password(length):
    """
    Generate a password with:
    - Mandatory '@' in the password.
    - Numbers can only appear after '@'.
    - No repeated characters.
    """
    lowercase = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special_chars = list('#&()_=+[]{}|;:,.<>?/')  # '@' handled separately
    numbers = list('0123456789')

    # Ensure password length is enough to hold '@' and at least one number
    if length < 7:
        raise ValueError("Password length must be at least 7 for this rule.")

    # Shuffle character pools
    random.shuffle(lowercase)
    random.shuffle(uppercase)
    random.shuffle(special_chars)
    random.shuffle(numbers)

    # Combine allowed characters except '@' and numbers
    all_chars = lowercase + uppercase + special_chars

    # Remove duplicates later: so keep track
    used_chars = set()

    # Select random characters before '@'
    before_at_length = length - 2  # 1 for '@', 1 for at least one number
    before_at = []

    while len(before_at) < before_at_length and all_chars:
        char = random.choice(all_chars)
        if char not in used_chars:
            before_at.append(char)
            used_chars.add(char)

    # Add '@'
    password = ''.join(before_at) + '@'

    # Select number(s) to add after '@'
    after_at = ''
    while len(password) + len(after_at) < length:
        num = random.choice(numbers)
        if num not in used_chars:
            after_at += num
            used_chars.add(num)

    return password + after_at


def copy_to_clipboard(password):
    """Copy password to clipboard."""
    pyperclip.copy(password)
    print("Password copied to clipboard.")


def main():
    """Main loop to generate multiple passwords, ensure user satisfaction, and stop with user permission."""
    print("Welcome to the Custom Password Generator!")

    while True:
        try:
            length = int(input("Enter password length (min 4, recommended 8+): ") or 8)

            print("\nGenerating 5 unique passwords for you:\n")
            passwords = []

            while len(passwords) < 5:
                pwd = generate_password(length)
                if pwd not in passwords:  # Ensure no duplicate passwords
                    passwords.append(pwd)
                    print(pwd)

            # Copy the first one by default
            copy_to_clipboard(passwords[0])

            satisfied = input("\nAre you satisfied with these passwords? (y/n): ").lower()

            if satisfied == 'y':
                print("Thank you for using the Password Generator!")
                break
            else:
                again = input("Do you want to generate again? (y/n): ").lower()
                if again != 'y':
                    print("Okay, thank you for using the Password Generator! Goodbye.")
                    break

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main() 
    '''
# This code is a custom password generator that ensures:
# - Each password contains a mandatory '@' character.
# - Numbers can only appear after the '@'.  
# - No repeated characters in the password.
# The user can specify the length of the password, with a minimum length of 4.
# The program generates 5 unique passwords and allows the user to copy the first one to the clipboard.
# The user can choose to generate new passwords or exit the program.

# this is my custom password generator code.
import random
import pyperclip
pass_len = int(input("Enter the length of the password: "))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$&_"
if pass_len > len(characters):
    print("Password length must be at least 7 characters.")
else:
    output = "".join(random.sample(characters, pass_len))
    pyperclip.copy(output)
    print(f"Generated Password: {output}")
 