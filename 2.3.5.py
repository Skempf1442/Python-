# defining the employee class 
class Employee:
    # getter and setter methods for employee attributes
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_number(self):
        return self.number
    
    def set_number(self, number):
        self.number = number


# defining the productionWorker subclass 
class ProductionWorker(Employee):
    # getter and setter methods for productionWorker attributes
    def get_shift(self):
        return self.shift
    
    def set_shift(self, shift):
        self.shift = shift
    
    def get_pay_rate(self):
        return self.pay_rate
    
    def set_pay_rate(self, pay_rate):
        self.pay_rate = pay_rate
    
    # method to display worker details
    def print_details(self):
        shift_str = "Day" if self.shift == 1 else "Night"
        print("\nDetails of Employee:")
        print("-" * 50)
        print(f"Name: {self.get_name()}")
        print(f"Employee Number: {self.get_number()}")
        print(f"Shift: {shift_str}")
        print(f"Pay Rate: {self.get_pay_rate()}")
        print("-" * 50)
# main script to prompt user for input and display the productionWorker details

def main():
    # prompting the user to enter employee details
    print("Enter the following details of the Employee")
    print("-" * 40)

    # user input
    name = input("Enter Employee Name: ")
    number = int(input("Enter Employee Number: "))
    pay_rate = float(input("Enter Pay Rate: "))
    shift = int(input("Enter Shift Number (1 for Day, 2 for Night): "))

    # create an instance of production worker
    worker = ProductionWorker()

    # set attributes using setter methods
    worker.set_name(name)
    worker.set_number(number)
    worker.set_shift(shift)
    worker.set_pay_rate(pay_rate)

    # display the details using the object's method
    worker.print_details()

# call the main function directly
main()