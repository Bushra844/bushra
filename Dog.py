class Dog:
    # Attributes:
    def __init__(self, name, breed):  # __init__ is a constructor
        self.name = name
        self.breed = breed
    # Method:
    def bark(self):
        print("Woof!")

# Create a dog object
my_dog = Dog("Buddy", "Golden Retriever")

# Access attributes:
print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever

# Call a method:
my_dog.bark()  # Output: Woof!