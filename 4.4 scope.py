# Conversions for US to metric system 
Pounds_To_Kilograms = 0.453592
Inches_To_Meters = 0.0254

def get_valid_number(prompt):
    try:
        user_input = input(prompt) 
        number = float(user_input)
        return number
    except ValueError:
        print("Please enter a valid number.")
        return get_valid_number(prompt)

def main():
    weight_pounds = get_valid_number("Please enter your weight in pounds: ")
    height_inches = get_valid_number("Please enter your height in inches: ")

    # Convert the weight and height to metric and calculate BMI 
    weight_kg = weight_pounds * Pounds_To_Kilograms
    height_m = height_inches * Inches_To_Meters 

    bmi = weight_kg / (height_m * height_m)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Healthy weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")

# Call the main function to execute the code
main()
