# calculator.py (simulated module)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# geometry.py (simulated module)
import math

def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_circle(radius):
    return math.pi * radius ** 2

# Main program using the modules
def main():
    print("Welcome to the Math Operations Program!")

    # Using the calculator module
    result_add = add(5, 3)
    print("Addition result:", result_add)

    result_subtract = subtract(10, 4)
    print("Subtraction result:", result_subtract)

    # Using the geometry module
    rectangle_area = area_of_rectangle(5, 3)
    print("Area of Rectangle:", rectangle_area)

    triangle_area = area_of_triangle(4, 2)
    print("Area of Triangle:", triangle_area)

    circle_area = area_of_circle(3)
    print("Area of Circle:", circle_area)

if __name__ == "__main__":
    main()  # Call the main function
