class Pet:
    vet_name = "Happy Tails Veterinary Clinic"
    
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    def get_owner_first_name(self):
        return self.__owner_first_name

    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    def get_owner_last_name(self):
        return self.__owner_last_name

    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def get_pet_id(self):
        return self.__pet_id

    def set_pet_id(self, value):
        self.__pet_id = value

    def get_pet_name(self):
        return self.__pet_name

    def set_pet_name(self, value):
        self.__pet_name = value

    def get_pet_type(self):
        return self.__pet_type

    def set_pet_type(self, value):
        self.__pet_type = value

    def display_pet_info(self):
        print(f"Veterinary Office: {Pet.vet_name}")
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")

def check_property(pet, property_name):
    return hasattr(pet, property_name)

def main():
    pet1 = Pet("John", "Doe", "001", "Rex", "Dog")
    pet2 = Pet("Jane", "Smith", "002", "Whiskers", "Cat")
    pet3 = Pet("Alice", "Brown", "003", "Goldie", "Fish")
    
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()

    print("\nUpdating pet information for pet1...\n")
    pet1.set_pet_name("Maximus")
    pet1.display_pet_info()

    print("\nChecking properties...\n")
    print(f"Does pet1 have 'owner_first_name'? {check_property(pet1, 'owner_first_name')}")
    print(f"Does pet2 have 'pet_color'? {check_property(pet2, 'pet_color')}")
    print(f"Does pet3 have 'pet_type'? {check_property(pet3, 'pet_type')}")

main()
