string = input("Enter a string: ")

def count_case(s):

    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper =upper + 1
        if char.islower():
            lower =lower+ 1
    return upper,lower

u,l = count_case(string)
print("Number of uppercase letters:", u)
print("Number of lowercase letters:", l)

