# immutable in python are those that cannot be changed after creation and their memory location cannot be changed, whenever they are changed a new memory location is created

# mutable in python are those that can be changed after creation and their memory location can be changed

x=10
print(id(x))

x+=10
print(id(x))



# this is a mutable and memory location cannot be changed, both points to the same memory
lst=[1,2,3]
print(id(lst))

lst.append(4)
print(id(lst))