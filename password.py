import random
import string

print("===== PASSWORD GENERATOR =====")

password_length = int(input("Enter password length: "))

all_characters = (
    string.ascii_letters +
    string.digits
)

generated_password = ""

for i in range(password_length):
    generated_password += random.choice(all_characters)

print("Generated Password:", generated_password)