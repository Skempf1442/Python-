def replace_artist(top_artists):
    """
    Function to replace an artist in the top_artists list.
    Prompts the user to enter an index and a new artist name.
    Handles ValueError and IndexError exceptions.
    """
    try:
        # Ask the user for the index of the artist to replace
        index = int(input("Enter the index of the artist to replace (0-9): "))

        # Check if the index is within the valid range of the list
        if index < 0 or index >= len(top_artists):
            raise IndexError("The index you entered is out of range.")
        
        # Ask the user for the new artist name
        new_artist = input("Enter the new artist name: ").strip()

        # Replace the artist at the given index
        top_artists[index] = new_artist

        # Print the updated list
        print("\nUpdated list of top artists:")
        print(top_artists)
    
    except ValueError:
        print("Error: Please enter a valid integer for the index.")
    except IndexError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An input error occurred: {e}")

def main():
    # Predefined list of top artists
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", 
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    # Display the list of top artists
    print("Top 10 Performing Artists:")
    for idx, artist in enumerate(top_artists, start=1):
        print(f"{idx}. {artist}")
    
    # Prompt the user to replace an artist
    replace_artist(top_artists)

if __name__ == "__main__":
    main()
