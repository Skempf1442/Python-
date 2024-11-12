class Person:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def display_info(self):
        return f"Name: {self.get_name()}\nAddress: {self.get_address()}\nAge: {self.get_age()}\nPhone: {self.get_phone()}\n"

person1 = Person("Alice Johnson", "123 Maple Street, Springfield", 28, "555-1234")
person2 = Person("Bob Smith", "456 Oak Avenue, Shelbyville", 34, "555-5678")
person3 = Person("Charlie Brown", "789 Pine Road, Capital City", 22, "555-9876")

print("Person 1 Info:")
print(person1.display_info())

print("Person 2 Info:")
print(person2.display_info())

print("Person 3 Info:")
print(person3.display_info())
