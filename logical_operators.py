number = float(input("Enter a number: "))
if number > 5:
    print("This number is greater than five.")

print('_________________')

x = float(input("x = "))

if x > 0:
    y = x ** 0.5
else:
    y = x ** 2
print(y)

print('_________________')

x = float(input("x = "))

if 0 < x < 7:
    print("Value is in range, let's continue")
    y = 2 * x - 5
    if y < 0:
        print("y - negative")
    elif y > 0:
        print("y - positive")
    else:
        print("y = 0")

print('_________________')

string = input('Enter a string: ')
if string:
    print('This string: {}'.format(string))
else:
    print('String is empty')