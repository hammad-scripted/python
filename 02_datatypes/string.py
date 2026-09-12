name="Alex"
age=26

# formatted strings

print(f"My name is {name} and I am {age} years old")


# note input always returns a string
user_name=input("Enter your name: ")
print(f"Hello {user_name}")


message="Hello World"
print(message[0])
# multiple lines strings
poem="""

Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

"""
print(poem)

# common strings operations

print(message.upper())
print(message.lower())
print(len(message))

greeting =" how are you  "
print(greeting.strip())


sentence ="I am learning python"

print(sentence.replace("python","and java"))