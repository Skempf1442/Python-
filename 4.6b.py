# The NATO alphabet dictionary
nato_alphabet = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

# Function to spell out the word using the NATO alphabet
def spell_word():
    user_word = input("Please enter a word: ")  # User enters a word
    user_word = user_word.upper()  # Converts to uppercase to match dictionary keys

    print("NATO Phonetic Spelling:")
    for letter in user_word:
        if letter in nato_alphabet:  # Check if the letter is in the dictionary
            print(nato_alphabet[letter])  # Prints the corresponding NATO word
        else:
            print(f"'{letter}' is not a valid letter.")

# Main function to call spell_word
def main():
    spell_word()

# Runs the main function
main()
