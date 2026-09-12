person={
    "name":"John",
    "age":30,
    "city":"New York"
}
print(person)

print(type(person))

print(person["name"])
print(person["age"])
print(person["city"])   

person["email"]="j7aMk@example.com" 

print(person)

print("\n")

for key,value in person.items():
    print(f"{key}:{value}")