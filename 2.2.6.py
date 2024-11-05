def main():
    # Step 1: Initialize an empty list for flowers
    flowers = []

    # Step 2: Prompt user to enter flowers, and stop when "done" is entered
    print("Enter flower names one by one. Type 'done' when you're finished.")
    while True:
        try:
            flower = input("Enter a flower name: ").strip()
            if flower.lower() == 'done':  # Stop the input loop when "done" is entered
                break
            elif flower:  # If the input is not empty
                flowers.append(flower)
            else:
                print("Please enter a valid flower name (cannot be empty).")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Step 3: Sort the list alphabetically and display the flowers
    flowers.sort()
    print("\nList of flowers (sorted):")
    for idx, flower in enumerate(flowers, start=1):
        print(f"{idx}. {flower}")

    # Step 4: Search for a specific flower
    try:
        search_flower = input("\nEnter the name of a flower to search for: ").strip()
        if search_flower in flowers:
            print(f"{search_flower} is found in the list!")
        else:
            print(f"{search_flower} was not found in the list.")
    except Exception as e:
        print(f"An error occurred while searching: {e}")

    # Step 5: Access a specific flower by number (1-based index)
    try:
        flower_number = int(input("\nEnter the number of the flower to access (1-based index): "))
        # Adjust the index for 0-based list indexing
        if 1 <= flower_number <= len(flowers):
            print(f"The flower at position {flower_number} is {flowers[flower_number - 1]}.")
        else:
            print(f"Error: The number {flower_number} is out of range. Please enter a valid number.")
    except ValueError:
        print("Error: Please enter a valid number.")
    except IndexError:
        print("Error: The index is out of range.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
