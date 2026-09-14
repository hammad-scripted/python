#  Decorators are those functions which either wrap another function or modify its behaviour or either return a function or return a value
def greet():
    return "Hello, world!"


my_func = greet
print(my_func())


def shout(func):
    return func().upper()


print(shout(my_func))
print(shout(greet))


def outer():
    def inner():
        print("Hello from inner function")

    return inner


new_func = outer()
new_func()


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_hello():
    print("Hello")


say_hello = my_decorator(say_hello)
say_hello()


@my_decorator
def say_hi():
    print("Hi")


say_hi()


from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"You called {func.__name__}")
        return func(*args, **kwargs)
    
    
    return wrapper

@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai")
    
    
brew_chai("black")



def my_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"You called {func.__name__} with args={args} and kwargs={kwargs}")
        result=func(*args,**kwargs)
        print(f"{func.__name__} returned {result}" )
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a+b

ans=add(2,3)
print(ans)       

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} took {end-start} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(2)
    return "Done!"


print(slow_function())