fixed_number = 10
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number: "))
    if guess == fixed_number:
        print("Congratulations! You guessed the number.")
        break
    else:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")
        if attempts == 0:
            print(f"sorry, you've used all attempts. the number was {fixed_number}")