import random
import string

print("\n======= SECURE PASSWORD GENERATOR =======")

while True:

    try:

        password_length = int(input("\nEnter password length: "))

        if password_length < 4:
            print("⚠ Password length should be at least 4.")
            continue

        include_symbols = input(
            "Include special characters? (yes/no): "
        ).lower()

        lower_case_letters = string.ascii_lowercase
        upper_case_letters = string.ascii_uppercase
        numeric_values = string.digits

        all_characters = (
            lower_case_letters +
            upper_case_letters +
            numeric_values
        )

        if include_symbols == "yes":
            all_characters += string.punctuation

        generated_password = ""

        for i in range(password_length):
            generated_password += random.choice(all_characters)

        print("\nGenerated Secure Password:")
        print(generated_password)

        repeat_choice = input(
            "\nGenerate another password? (yes/no): "
        ).lower()

        if repeat_choice != "yes":
            print("\nPassword Generator Closed Successfully.")
            break

    except ValueError:
        print("\n⚠ Please enter a valid numeric value.")