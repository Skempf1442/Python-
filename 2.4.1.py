# Define the generator function for two-letter combinations
def two_letter_combinations(characters):
    """
    Generator function to yield all possible two-letter combinations
    from the given list of characters.
    """
    for first in characters:
        for second in characters:
            yield first + second  # Use yield to create a generator

def main():
    """
    Main function to demonstrate the generator functionality.
    Calls the generator with a custom list of characters and
    prints all combinations.
    """
    # Define a 5-letter list of characters
    characters = ['a', 'b', 'c', 'd', 'e']
    
    # Call the generator and print each combination
    print("All possible two-letter combinations:")
    for combination in two_letter_combinations(characters):
        print(combination)

# Run the main function
if __name__ == "__main__":
    main()
