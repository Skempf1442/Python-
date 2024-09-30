# Simple Python program to calculate the square of a number
def square_number():
    while True:
        try:
            number = input("Enter a number to square: ")
            squared_number = int(number) ** 2
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        else:
            print(f"The square of {number} is {squared_number}.")
            break
        finally:
            print("Execution of the square_number function completed.")

# Call the function
square_number()
