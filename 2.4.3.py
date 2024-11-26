import os

def main():
    print(f"Current working directory: {os.getcwd()}")  # Displays the working directory for debugging
    try:
        with open('sales_totals.txt', 'r') as file:  # Ensure the file is in the same directory
            total = 0.0
            count = 0

            print("Sales Totals:")
            for line in file:
                line = line.strip()  # Remove extra whitespace or newline characters
                if line:  # Process only non-empty lines
                    number = float(line)
                    print(f"{number:,.2f}")  # Format the number for display
                    total += number
                    count += 1

            if count > 0:
                average = total / count
            else:
                average = 0.0

            print(f"\nTotal: {total:,.2f}")
            print(f"Number of entries: {count}")
            print(f"Average: {average:,.2f}")

    except FileNotFoundError:
        print("Error: The file 'sales_totals.txt' was not found.")
    except ValueError:
        print("Error: One or more lines in the file could not be converted to a float.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
