import random
import string

length = int(input("Enter the password length: "))

characters = ""

if input("Include uppercase letters? (y/n): ").lower() == "y":
    characters += string.ascii_uppercase

if input("Include lowercase letters? (y/n): ").lower() == "y":
    characters += string.ascii_lowercase

if input("Include numbers? (y/n): ").lower() == "y":
    characters += string.digits

if input("Include special characters? (y/n): ").lower() == "y":
    characters += string.punctuation

if characters:
    password = "".join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
else:
    print("Please select at least one character type.")