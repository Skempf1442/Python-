#function to convert numeric grade to letter grade 
def get_letter_grade(numeric_grade):
    if numeric_grade >=90:
        return 'A'
    elif numeric_grade >=80:
        return 'B'
    elif numeric_grade>=70:
        return 'C'
    elif numeric_grade>=60:
        return 'D'
    else:
        return 'F'
    
#Input numeric grade
numeric_grade = 95

letter_grade = get_letter_grade(numeric_grade)
print(f"The letter grade for {numeric_grade} is: {letter_grade}")