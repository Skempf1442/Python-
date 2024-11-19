class Pet:
    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        self.kind = kind

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        self.breed = breed

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def print_details(self):
        print(f"Pet Details: Kind={self.kind}, Breed={self.breed}, Name={self.name}")


pet1 = Pet("Dog", "Labrador", "Buddy")
pet2 = Pet("Cat", "Siamese", "Whiskers")
pet3 = Pet("Bird", "Parrot", "Polly")

print("\n--- Pet Details ---")
pet1.print_details()
pet2.print_details()
pet3.print_details()

print("\n--- Demonstrating Special Methods ---")
print(f"Class Name: {Pet.__name__}")
print(f"Type of pet1: {type(pet1)}")
print(f"Module Name: {Pet.__module__}")
print(f"Base Classes of Pet: {Pet.__bases__}")
print(f"Pet1's Name using getattr(): {getattr(pet1, 'name')}")
print(f"Is pet1 an instance of Pet? {isinstance(pet1, Pet)}")
