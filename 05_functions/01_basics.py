def greet():
    print("Hello")

greet()
greet()
greet()


# function with parameters

def greet(name):
    print(f"Hello {name}")

greet("Alice")
greet("Bob")

def add(a,b):
    print(a+b)

add(2,3)


def add(a,b):
    return a+b

result=add(2,3)
print(result)

def square(x):
    return x*x

ans=square(5)
print(ans)


# keyword arguments

def introduce(name,age,city):
    print(f"Hi, my name is {name}, I am {age} years old and I live in {city}")


# positional arguments

introduce("Alice", 25, "New York")
introduce("Bob", 30, "London")

# keyword arguments : order does not matter

introduce(name="Alice", age=25, city="New York")
introduce(age=30, city="London", name="Bob")

# Mixing positional and keyword arguments
# If you mix positional and keyword arguments, the keyword arguments will override the positional arguments and generally positional should come first otherwise it will throw an error