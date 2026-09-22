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
make_animal_speak(Animal())  # Output: Generic animal sound

#method overloading

print("method overloading")

# example

class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
    

calc = Calculator()
print(calc.add(1, 2))  # Output: 3
print(calc.add(1, 2, 3))  # Output: 6       

