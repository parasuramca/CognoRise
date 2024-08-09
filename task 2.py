def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return "Error! Division by zero." if y == 0 else x / y
def calculator():
    print("Simple Calculator\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        op = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        op = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        op = '*'
    elif choice == '4':
        result = divide(num1, num2)
        op = '/'
    else:
        print("Invalid input")
        return
    print(f"{num1} {op} {num2} = {result}")
calculator()
