import random
import string

print("===== PASSWORD GENERATOR =====")

try:

    password_length = int(input("Enter password length: "))

    include_symbols = input("Include special characters? (yes/no): ").lower()

    all_characters = (
        string.ascii_letters +
        string.digits
    )

    if include_symbols == "yes":
        all_characters += string.punctuation

    generated_password = ""

    for i in range(password_length):
        generated_password += random.choice(all_characters)

    print("Generated Password:", generated_password)

except ValueError:
    print("Please enter a valid numeric length.")