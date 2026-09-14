squares_list=[x**2 for x in range(1,11)]

squares_gen=(x**2 for x in range(1,11))

print(squares_list)
print(squares_gen)

# generators need to be consumed, they produce items one at a time and are memory efficient
for val in squares_gen:
    print(val)
    


gen=(x for x in range(1,5))

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))    

# generators can only be consumed once
print(list(gen))
print(list(gen))