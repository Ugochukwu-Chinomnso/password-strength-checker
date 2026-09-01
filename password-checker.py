from getpass import getpass
import unicodedata

password = getpass("Enter your password: ")
length = len(password)

if length < 8:
    print("Password is too short. It must be at least 8 characters long.")

has_digit = any(char.isdigit() for char in password)

if not has_digit:
    print("Password must contain at least one number.")

has_uppercase = any(char.isupper() for char in password)

if not has_uppercase:
    print("Password must contain at least one uppercase letter.")

has_symbol = any(
    unicodedata.category(char).startswith(("S", "P"))
    for char in password
)

if not has_symbol:
    print("Password must contain at least one special character.")

score = sum([
    length >= 8,
    has_digit,
    has_uppercase,
    has_symbol,
])

print(f"Password strength score: {score}/4")

if score <= 1:
    print("Password Strength: Weak")
elif score <= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")