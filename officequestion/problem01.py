user_input = input("enter a value: ")

if user_input.isnumeric():
    num = int(user_input)
    print('Datatype', type(num))

    if num % 2 == 0:
        print(f"the number {num} is even")
    else:
        print(f"the number {num} is odd")
else:
    print("invalid input")