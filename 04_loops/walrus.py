# The walrus operator (:=), officially known as the assignment expression operator, was introduced in Python 3.8. It allows you to assign a value to a variable as part of a larger expression.


# print(x=5) # error
print(x:=5)
# In standard Python, a regular assignment (=) is a statement, meaning it performs an action but does not return a value. The walrus operator (:=) is an expression, meaning it assigns the value and immediately returns that value.


# foods=[]

# while True:
#     food=input("Enter a food you like or q to quit: ")
#     if food=="q":
#         break
#     foods.append(food)

# print(foods)

foods=[]

while(food:=input("Enter a food you like or q to quit: "))!="q":
    foods.append(food)

print(foods)