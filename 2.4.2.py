def main():
    try:
        date = input("Enter the current date (e.g., 2024-11-19): ")
        time = input("Enter the current time (e.g., 14:30): ")
        entry = input("Enter your diary entry: ")
        
        with open('diary.txt', 'a') as file:
            file.write(f"Date: {date}\nTime: {time}\n")
            file.write(f"Entry: {entry}\n")
            file.write("\n")
        
        print("Your entry has been saved successfully!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
