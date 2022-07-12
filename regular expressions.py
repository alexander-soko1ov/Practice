import re

text = "Карта map и объект bitmap - это разные вещи"

result = re.findall(r"\bmap\b", text)

print(result)