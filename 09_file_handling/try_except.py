try:
    number=int(input("Enter a number:"))
    result=10/number
    print(result)

except ZeroDivisionError:
    print("You cannot divide by zero")

except ValueError:
    print("Invalid input")

except Exception:
    print("Something went wrong")
    
finally:
    print("This will always execute")
    


try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered {number}, nice!")   # only runs if try succeeded
    
try:
    my_list=[1,2,3,4,5]
    print(my_list[10])
except IndexError:
    print("Index out of range")