import arrow
from datetime import datetime
# '2018.04.29T17:45:25Z'
# '2022.07.18'

dt = arrow.get(input('Введите дату и время: '))

# print(dt)
print("\nВы ввели:")
print(dt.date())
print(dt.time())

print("\nСейчас:")

print(datetime.now().date())
print(datetime.now().time())

print("\nОсталось времени:", dt.date() - datetime.now().date())
print("\nОсталось времени:", dt.time() - datetime.now().time())