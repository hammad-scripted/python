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

# multiple return values

def get_name_and_age():
    return "Alice", 25


name, age = get_name_and_age()
print(name)
print(age)


# args and kwargs
# args accept any number of positional arguments

def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4, 5)


def add_all(*args):
    print(args) # its an tuple
    return sum(args)


result = add_all(1, 2, 3, 4, 5)
print(result)


# kwargs accept any number of keyword arguments

def print_info(**details):
    # details is a dictionary of key-value pairs
    print(details)
    for key,value in details.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

# docstring - description of a function

def divide(a,b):
    """
    Divides two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        float: The result of the division.
    """

    return a/b


print(divide.__doc__)
print(divide(10,5))




def calculate_bmi(weight_kg,height_m):

    """
    Calculates the Body Mass Index (BMI) based on weight and height.    
    """
    bmi=weight_kg/(height_m**2)

    if bmi<18.5:
       category="Underweight"
    elif bmi<25:
       category="Normal weight"
    else:
       category="Overweight"

    return round(bmi,2),category


bmi,category=calculate_bmi(70,1.75)
print(f"Your BMI is {bmi} and you are {category}")