n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")


list1 = [2,3,4,5,6]

print("length is ", len(list1))

for d in range(len(list1)-1):
    print("--->",list1[d])