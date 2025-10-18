# Simple Password Generator Project

import random
import string

print("=== PASSWORD GENERATOR ===")


length = int(input("Enter desired password length: "))


include_special = input("Include special characters? (yes/no): ").lower()


letters = string.ascii_letters  # A-Z and a-z
digits = string.digits          # 0-9
specials = string.punctuation   # !@#$%^&*()


if include_special == "yes":
    all_characters = letters + digits + specials
else:
    all_characters = letters + digits


password = ''.join(random.choice(all_characters) for i in range(length))


print("\nYour generated password is:", password)
print("Keep it safe! 🔒")
