

def get_squares(n):
    result=[]
    for i in range(n):
        result.append(i**2)
    return result

print(get_squares(10))


def get_squares(n):
    for i in range(n):
        yield i**2
        
gen=get_squares(10)
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# return ends the function completely. yield pauses the function, remembering exactly where it was — variables, loop position, everything — until you ask for the next value.

def countdown(n):
    print("Starting countdown")
    while n>0:
        yield n
        n-=1
    print("done")
    
gen=countdown(3)
print(next(gen))
print(next(gen))
print(next(gen))


def indefinite_counter():
    n=1
    while True:
        yield n
        n+=1

# for i in indefinite_counter():
#     print(i)
    

def fibonacci(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

for num in fibonacci(10):
    print(num,end=" ")