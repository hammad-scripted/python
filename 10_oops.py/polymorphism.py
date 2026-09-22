class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof! 🐶")

class Cat(Animal):
    def speak(self):
        print("Meow! 🐱")

# The correct method is resolved at runtime based on the object
def make_animal_speak(animal_object):
    animal_object.speak()

make_animal_speak(Dog())  # Output: Woof!
make_animal_speak(Cat())  # Output: Meow!
