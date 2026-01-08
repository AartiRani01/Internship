n = int(input("Enter a number: "))
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n + sum_digits(n-1)

print(sum_digits(n))