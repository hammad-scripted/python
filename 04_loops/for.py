for i in range(5):
    print(i)
    # output 0 1 2 3 4(starts at 0, ends at 4)


for i in range(2,6):
    print(i)
    # output 2 3 4 5

for i in range(10, 0, -1):
    print(i)




# enumerate() - get index +value together

fruits=["apple","banana","cherry","kiwi","mango"]

for index,fruit in enumerate(fruits):
    print(index,fruit)

    