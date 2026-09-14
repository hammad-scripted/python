numbers=[1,2,3,4,5]
squares={n:n*n for n in numbers}
print (squares)

names=["Alex","Sam","Jordan"]
names_length={name:len(name) for name in names}
print(names_length)

prices={"apple":2.99,"banana":1.99,"orange":1.49}

expensive={k:v for k,v in prices.items() if v>1.5}
print(expensive)