class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Create an instance of the Person class
person = Person(name="Erick", age=30, gender="Male")

# Call the introduce method
person.introduce()
