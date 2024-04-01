import re

user_input = input()

pattern = r"\b(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(pattern, user_input)

for el in matches:
    print(f'Day: {el[0]}, Month: {el[2]}, Year: {el[3]}')
