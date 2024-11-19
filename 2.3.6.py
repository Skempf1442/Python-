# Custom exception class
class NotNumericError(Exception):
    """Exception raised when the input is not a number."""
    def __init__(self, input_value, message="Input must be numeric."):
        self.input_value = input_value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"'{self.input_value}' -> {self.message}"

# Main program logic
def main():
    while True:
        try:
            # Prompt the user for input
            user_input = input("Enter a number: ")
            
            # Validate if the input is numeric
            if not user_input.isnumeric():
                raise NotNumericError(user_input)
            
            # If input is valid, print a confirmation message
            print(f"Valid input! You entered the number: {user_input}")
            break  # Exit the loop when valid input is received
        
        except NotNumericError as e:
            # Handle the NotNumericError exception
            print(f"Error: {e}")
        
        else:
            # This block executes if no exceptions occur
            print("Input successfully validated.")
        
        finally:
            # Always runs to indicate end of iteration
            print("End of this iteration.\n")

# Run the main program
if __name__ == "__main__":
    main()
