class Dog:
    def bark(self):
        print("woof woof")

# creating an object and these tow objects are instances of the Dog class which are distinct
my_dog=Dog()
your_dog=Dog()
print(type(my_dog))
print(type(your_dog))
print(id(my_dog))
print(id(your_dog))


# adding attributes to objects
my_dog.name="Fido"
my_dog.breed="Lab"
my_dog.age=3

print(my_dog.name)
print(my_dog.breed)
print(my_dog.age)

# adding behaviour to objects
my_dog.bark()
your_dog.bark()