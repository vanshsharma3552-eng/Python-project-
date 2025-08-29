import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define possible characters
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = letters + digits + symbols

    # Randomly choose characters for password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def main():
    print("🔐 Password Generator 🔐")
    print("========================")

    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print("\nGenerated Password:")
        print(password)
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
