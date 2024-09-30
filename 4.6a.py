def main():
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials',  'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')
    
    # Loop through each class and print the class name
    for course in programming_classes:
        print(course)
    
    # Print the total number of classes
    print(f"\nThese are the {len(programming_classes)} programming classes offered.")
    
# Call the main function to execute the program
main()
