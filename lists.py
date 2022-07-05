int_list = [1, 2, 3, 4]
print(int_list)

list_from_range = list(range(7))
print("From range:", list_from_range)

list_from_string = list("a string")
print("From string", list_from_string)

print(list_from_range[0])
print(list_from_string[4])

sub_list = list_from_range[1:4]
print(sub_list)

sub_list = list_from_range[:-4]
print(sub_list)

sub_list = list_from_range[:-2:2]  #[начальное значение: конечное значение: шаг]
print(sub_list)

print(6 in list_from_range)
print('Length:', len(list_from_range))

print('______________________')

my_list = [2, 6, 1, 8, 3, 9, 7]
print(my_list,'\n')

del my_list[5]
print('del:', my_list)

my_list[4] = 22
print('change', my_list)

print('______________________')

for x in my_list:
    print("{} ^ 2 = {}".format(x, x ** 2))

print('______________________')

print('Fibonacci numbers')

n = 10

fib = [1, 1]

for i in range(n - 2):
    fib.append(fib[i]+fib[i+1])

print(fib)