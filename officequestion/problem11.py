operands1 = float(input('Enter first number: '))
operands2 = float(input('Enter second number: '))
op = input('Enter operator (+, -, *, /, %): ')

def calculate(opr1,opr2,opr3='*'):
    if opr3 == '+':
        result = opr1 + opr2
    elif opr3 == '-':
        result = opr1 - opr2
    elif opr3 == '*':
        result = opr1 * opr2
    elif opr3 == '/':
        if opr2 != 0:
            result = opr1 / opr2
        else:
            print("Error: Division by zero is not allowed.")
            result = None

    if result is not None:
        print("Result:", result)



calculate(operands1, operands2)
    


#calculate(operands1, operands2, op)