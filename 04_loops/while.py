cnt=0

while cnt<=5:
    print(cnt)
    cnt+=1




for num in range(2,10):
    if num%7==0:
        print(f"Found a multiple of 7: {num}")
        break
else:
    print("No multiples of 7 found")


for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}") 