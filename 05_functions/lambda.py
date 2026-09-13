
def add(a,b):
    return a+b

# anonymous function - lambda
add=lambda a,b:a+b
print(add(2,3))

square= lambda x:x*x
print(square(5))

multiply=lambda a,b:a*b
print(multiply(2,3))


# map
numbers=[1,2,3,4,5]

squared=map(lambda x:x*x,numbers)
print(squared)
print(list(squared))

multiply=map(lambda x,y:x*y,numbers,numbers)
print(multiply)
print(list(multiply))

a=[1,2,3]
b=[4,5,6]
add=list(map(lambda x,y:x+y,a,b))
print(add)


names=["alex","bob","charlie"]

upper_name=[]

for name in names:
    upper_name.append(name.upper())

print(upper_name)

upper_name=list(map(lambda name:name.upper(),names))
print(upper_name)