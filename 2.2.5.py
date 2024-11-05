import re  # Importing the regex module for pattern matching

def is_valid_password(password):
    """
    Checks if the password meets the following criteria:
    1. Length between 8 and 20 characters
    2. Contains at least one uppercase letter
    3. Contains at least one lowercase letter
    4. Contains at least one number
    5. Contains at least one special symbol from !@#$%&*
    """
    # Check password length
    if not (8 <= len(password) <= 20):
        return False

    # Check for at least one uppercase letter
    if not any(c.isupper() for c in password):
        return False

    # Check for at least one lowercase letter
    if not any(c.islower() for c in password):
        return False

    # Check for at least one digit
    if not any(c.isdigit() for c in password):
        return False

    # Check for at least one special symbol from the allowed set
    if not any(c in "!@#$%&*" for c in password):
        return False

    # If all conditions are met, the password is valid
    return True

def main():
    """
    Main function to prompt the user for a password, validate it,
    and confirm the password by asking for it a second time.
    """
    while True:
        try:
            # Prompt user to enter a password
            password = input("Enter a password (8-20 characters, at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 symbol): ").strip()

            # Validate the password
            if is_valid_password(password):
                print("Password is valid.")
                
                # Ask the user to confirm the password
                confirm_password = input("Confirm your password: ").strip()

                # Check if the confirmation matches the original password
                if password == confirm_password:
                    print("Password confirmed successfully!")
                    break  # Exit the loop if passwords match and are valid
                else:
                    print("Passwords do not match. Please try again.")

            else:
                print("Password does not meet the required criteria. Please try again.")
        
        except Exception as e:
            # Handle unexpected exceptions
            print(f"An error occurred: {e}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
