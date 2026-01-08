user_input = int(input("enter your number is: "))
book_price = int(input("enter the book price is: "))
#issued_date = int(input("enter the issued date is: "))
#return_date = int(input("enter the return date is: "))
#input_field = int(input("inputfield is, daydifference is: ")))

if user_input == 2:
    print("no fine")
elif user_input >= 2 and user_input < 5:
    fine = book_price * 10 / 100
    print("the fine amount is:", fine)
elif user_input >= 5 and user_input <= 7:
    fine = book_price * 12 / 100
    print("the fine amount is:", fine)
elif user_input >= 7:
    fine = book_price * 20 / 100
    print("the fine amount is:", fine)
else:
    print("invalid input")