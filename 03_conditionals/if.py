age=20
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



score=75

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")      


a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)



age=17
has_license=True

if age>=18 and has_license:
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")

# Truthy and falsy values

# falsy values
if 0:print("won't print")
if "":print("won't print")
if []:print("won't print")
if {}:print("won't print")
if None:print("won't print")

# truthy values
if 1:print("will print")
if "a":print("will print")
if [1,2]:print("will print")

