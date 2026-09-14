#  Decorators are those functions which either wrap another function or modify its behaviour or either return a function or return a value
def greet():
    return "Hello, world!"

my_func=greet
print(my_func())


def shout(func):
    return func().upper()

print(shout(my_func))
print(shout(greet))


def outer():
    def inner():
        print("Hello from inner function")
    return inner


new_func=outer()
new_func();



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello")
    
say_hello=my_decorator(say_hello)
say_hello()

@my_decorator
def say_hi():
    print("Hi")
    
say_hi()