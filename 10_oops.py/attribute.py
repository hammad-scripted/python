# instance attribute are unique to each object

class Dog:
    species="Canis Familiaris" # class attribute
    
    def __init__(self,name):
        self.name=name  

dog1=Dog("Fido")
dog2=Dog("Buddy")

print(dog1.species)
print(dog1.species)



class Cat:
    species="Felis Catus"
    
    

cat1=Cat()
cat2=Cat()

print(cat1.species)
print(cat2.species)
#this will create a new  instance attribute related to cat1
cat1.species="Persian"
print(cat1.species)
print(cat2.species)
# if we want to actually change the class attribute we have to use class name
Cat.species="Modifies species"

print(cat1.species)
print(cat2.species)

