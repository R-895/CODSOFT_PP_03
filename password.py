import random
import string

def generate_password(length):
    # Use a combination of letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    print("Welcome to the Password Generator")
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
