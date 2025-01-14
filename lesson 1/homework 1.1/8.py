def calculator():

    a = float(input("Enter the first number (a): "))


    b = float(input("Enter the second number (b): "))


    operation = input("Enter the operation (+, -, *, /): ")


    if operation == '+':
        result = a + b
        print(f"The result of {a} + {b} is: {result}")
    elif operation == '-':
        result = a - b
        print(f"The result of {a} - {b} is: {result}")
    elif operation == '*':
        result = a * b
        print(f"The result of {a} * {b} is: {result}")
    elif operation == '/':
        if b == 0:
            print("Division by zero")
        else:
            result = a / b
            print(f"The result of {a} / {b} is: {result}")
    else:
        print("Invalid operation")



calculator()