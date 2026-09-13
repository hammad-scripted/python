numbers=[1,2,3,4,5,6,7,8,9,10]

evens=list(filter(lambda x:x%2==0,numbers))
print(evens)

words=["apple","","cherry","kiwi","","orange","","strawberry","watermelon"]

non_empty=list(filter(None,words))
print(non_empty)


students=[
    {"name":"Alice","age":20,"grade":"A"},{"name":"Bob","age":19,"grade":"B"},{"name":"Charlie","age":21,"grade":"C"},
    {"name":"Dave","age":22,"grade":"D"},{"name":"Eve","age":20,"grade":"E"},{"name":"Frank","age":19,"grade":"F"}  
]

passed=list(filter(lambda student:student["grade"]!="F",students))
print(passed)