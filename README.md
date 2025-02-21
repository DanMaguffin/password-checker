# Password Strength Checker
A Python script to evaluate password strength based on multiple criteria.

## Features
- Checks for 12+ characters
- Requires uppercase, lowercase, numbers, and special characters
- Rejects common passwords (e.g., "password123", "admin")
- Saves results to a text file (password_results.txt)

## Tools Used
- Python 3
- Regular expressions (re module)

## How to Run
1. Install Python from python.org
2. Run `python password_checker.py`
3. Enter a password (type 'quit' to exit)

## Example Output
- Input: `password123`
- Output: `Password is too common - choose something unique`
- Input: `SecureP@ssw0rd123`
- Output: `Password is strong!`
