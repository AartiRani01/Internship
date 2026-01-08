user_input = input("enter a number: ")

if user_input.isnumeric():
    last_digit = int(user_input [-1])

    if last_digit % 3 == 0:
        print(f"the number {user_input} is divisible by 3")
    else:
        print(f"the number {user_input} is not divisible by 3")
else:
    print("invalid input")        