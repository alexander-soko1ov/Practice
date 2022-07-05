import math

x = float(input('1 number: '))
y = float(input('2 number: '))
operation = input('Operation: ')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '^':
    result = x ** y
elif operation == 'sqrt':
    result = math.sqrt(x)
else:
    print('Unsupported operation')

if result is not None:
    print('Result:', result)