import re

def check_password(password):
    # Check for common passwords
    common_passwords = ["password123", "admin", "123456", "qwerty", "letmein"]
    if password.lower() in common_passwords:
        return "Password is too common - choose something unique"
    
    # Check length
    if len(password) < 12:
        return "Password too short (minimum 12 characters)"
    
    # Check for uppercase, lowercase, numbers, and special characters
    if not re.search(r"[A-Z]", password):
        return "Missing uppercase letters"
    if not re.search(r"[a-z]", password):
        return "Missing lowercase letters"
    if not re.search(r"[0-9]", password):
        return "Missing numbers"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Missing special characters"
    
    # If all checks pass
    return "Password is strong!"

# Test the function and save results
def main():
    print("Enter a password to check its strength (or 'quit' to exit):")
    while True:
        user_password = input("> ")
        if user_password.lower() == "quit":
            break
        result = check_password(user_password)
        print(result)
        
        # Save to file
        with open("password_results.txt", "a") as file:
            file.write(f"Password: {user_password}, Result: {result}\n")

if __name__ == "__main__":
    main()