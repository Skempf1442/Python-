def main():
    # Prompt for User Input
    user_input = input("Enter a character: ")

    # Validate the Input
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")

    # Convert to ASCII Value
    ascii_value = ord(user_input)

    # Display the Result
    print(f"The ASCII value of '{user_input}' is {ascii_value}")

# Run the main function
if __name__ == "__main__":
    main()
