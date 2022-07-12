import re

# text = "Карта map и объект bitmap - это разные вещи"
# result = re.findall(r"\bmap\b", text)

text = "Еда, беду, победа, 25:15, 6, 1:12"
result = re.findall(r"[0-9]?[0-9]:\d{2}", text)

print(result)