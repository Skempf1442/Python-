def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        user_input = input("Please enter a non-negative integer: ")
        n = int(user_input)

        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return 
        result = factorial(n)
        print(f"The factorial of {n} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")

# Call the main function to execute the code
main()
