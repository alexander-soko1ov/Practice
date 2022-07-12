for i in range(2):
    print (f'hello world \n {i}')

print('End')

print('_____________________')

# Типы данных

string = "123456789"
numbers = int(string)
print('string nombers:', numbers + 100)

bool1 = True
bool2 = False

print('bool1:', bool1)
print('bool2:', bool2)

x = 3.1235
print(x, type(x))

print(complex(3, 5))
print(complex("5-9j"))

print('_____________________')

# Библиотека math

import math

x = 2.1546

print('x =', x)
print('trunc(x):', math.trunc(x))
print('floor(x):', math.floor(x))
print('ceil(x):', math.ceil(x))

print(math.pi)
print(math.e)

print(math.sqrt(64))