import re

pattern = r'[\w\.-]+@[\w-]+\.[a-zа-я]{2,9}'

def is_valid_email(sequence):
    pattern = r'[\w\.-]+@[\w-]+\.[a-zа-я]{2,9}'
    return bool(re.search(pattern, sequence))

long_sequence = """"
cfasd@mail.ru
supe.crsan.@internet.рф
asdbala@yahoo.education
an-jfas@123.1231.12321
"""

print(re.findall(pattern, long_sequence))