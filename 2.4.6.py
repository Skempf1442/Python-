import calendar
from datetime import datetime

def main():
    try:
        current_year = datetime.now().year
        birth_month = int(input("Enter your birth month as an integer (1-12): "))
        
        if 1 <= birth_month <= 12:
            print(calendar.month(current_year, birth_month))
        else:
            print("Invalid input. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
