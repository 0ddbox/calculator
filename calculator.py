def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "error: division by zero"
    return x / y

def multiply(x, y):
    return x * y

def calculator():
    print('welcome to the calculator')
    print('choose an operation')
    print('add')
    print('subtract')
    print('multiply')
    print('divide')

    while True:
        choice = input('choose an operation or quit: ')

        if choice == 'quit':
            print('goodbye')
            break

        if choice not in ('add', 'subtract', 'multiply', 'divide'):
            print('invalid, choose again')
            continue

        num1 = float(input('enter your first number: '))
        num2 = float(input('enter your second number: '))

        if choice == 'add':
            print('result: ', add(num1, num2))
        elif choice == 'subtract':
            print('result: ', subtract(num1, num2))
        elif choice == 'multiply':
            print('result: ', multiply(num1, num2))
        elif choice == 'divide':
            print('result: ', divide(num1, num2))

while True:
    calculator()