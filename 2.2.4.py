def main():
    # List to store the book titles
    book_titles = []
    
    # Loop to collect 10 book titles from the user
    while len(book_titles) < 10:
        title = input(f"Enter book title {len(book_titles) + 1}: ")
        # Capitalize the title properly before adding it to the list
        book_titles.append(title.strip().title())
    
    # Create a sorted list of book titles
    sorted_titles = sorted(book_titles)
    
    # Display the sorted book titles
    print("\nHere are your book titles in alphabetical order:")
    for title in sorted_titles:
        print(title)

# Call the main function to run the program
if __name__ == "__main__":
    main()
