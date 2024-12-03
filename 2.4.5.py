from datetime import datetime, timedelta

def main():
    try:
        year = int(input("What year were you born? "))
        month = int(input("What month were you born (as a number, e.g., May = 5)? "))
        day = int(input("What day of the month were you born? "))
        
        birthday = datetime(year, month, day)
        print(f"Your birthday is: {birthday.strftime('%Y-%m-%d')}")
        
        now = datetime.now()
        difference = now - birthday
        print(f"Difference is {difference.days} days")
        
        years = difference.days / 365.25
        print(f"You are {years:.1f} years old")
        
        months = years * 12
        print(f"You are approximately {int(months)} months old")
        
        weeks = difference.days // 7
        print(f"You are approximately {weeks} weeks old")
        
        hours = difference.total_seconds() / 3600
        print(f"You are approximately {int(hours)} hours old")
        
        minutes = difference.total_seconds() / 60
        print(f"You are approximately {int(minutes)} minutes old")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers for your birth date.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
