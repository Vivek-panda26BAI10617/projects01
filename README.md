# Password Generator
Simple Python Password Generator A beginner project that generates random passwords using the Python secrets module.

Features:
- Custom password length
- Minimum length validation
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Ensures that there is at least one character from each category
- Secure random character selection
- Secure shuffling
- Handles invalid user input
- Includes basic unit tests

Why secrets instead of random?
This project was originally implemented with Python's 'random' module.
That's great for learning about randomness, but it is NOT suitable for security-related uses.
In this approach, the Python relies on a native method secrets that is designed for creating tokens and passwords.
No external packages are required.

Project Structure

``text

password-generator/
password_generator.py
testpasswordgenerator.py
README.md
requirements.txt

`

Requirements:
- Python 3.8 or newer
- No third-party packages

`bash

cd password-generator

`

Run the program:

`bash

python password_generator.py

`

On some systems:

`bash

python3 password_generator.py

`

Example:

`text

=========================

Password Generator

=========================

Enter password length (minimum 4): 16

Your password is:

x7@Qm2#L_p9A!k4Z

`

The password created will be on a different basis.

Run Tests

Run:

`bash

python -m unittest testpasswordgenerator.py

`

If all goes well, they will pass.

Concepts Practiced

This project demonstrates:
- Functions
- User input
- Exception handling
- if statements
- for` loops
- Lists
- Strings
- String methods
- Python modules
- Unit testing
- Secure random generation

Future Improvements

Possible upgrades:
- Add a password-strength meter
- Add options to include/exclude character types
- Add a graphical user interface
- Add command-line arguments
- Add a "copy to clipboard" option
- Generate multiple passwords at once
  
Disclaimer
This is a learning project. Besides secrets, password security also relies on how passwords are stored, transmitted and used.

License

MIT License
