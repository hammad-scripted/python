# [expression for item in iterable]


squares=[]
for x in range(1,11):
    squares.append(x**2)

print(squares)

squares=[x**2 for x in range(1,11)]
print(squares)


numbers=range(1,11)

evens=[ x for x in numbers if x%2==0]
print(evens)


words=["apple","banana","cherry","kiwi","mango"]

long_words=[w for w in words if len(w)>=5]
print(long_words)


labels=["even" if n%2==0 else  "odd" for n in numbers]
print(labels) 