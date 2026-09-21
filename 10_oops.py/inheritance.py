# inheritance in python

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes a sound")
        

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def bark(self):
        print(f"{self.name} barks")
        
dog=Dog("Fido")
dog.speak()
dog.bark()