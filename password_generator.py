import secrets
import string


def generate_password(length):
    """Generate a secure random password."""
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%&*?+-_"

    # Guarantee at least one character from every group.
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special),
    ]

    all_characters = uppercase + lowercase + digits + special

    # Fill the remaining positions.
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Securely shuffle the password characters.
    for i in range(len(password) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password[i], password[j] = password[j], password[i]

    return "".join(password)


def main():
    print("=========================")
    print("    Password Generator")
    print("=========================")

    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))

            if length < 4:
                print("Password must be at least 4 characters.")
                continue

            password = generate_password(length)

            print("\nYour password is:")
            print(password)
            break

        except ValueError:
            print("Please enter a valid whole number.")


if __name__ == "__main__":
    main()
