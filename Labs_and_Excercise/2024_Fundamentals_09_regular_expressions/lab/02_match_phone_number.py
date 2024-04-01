import re

regex = r"(\+[3][5][9])([\s-])([2])(\2)(\d{3})(\2)(\d{4})\b"

test_str = input()

matches = re.findall(regex, test_str)
list_matches = []
for tup in matches:
    matches = []
    for num in tup:
        matches.append(num)
    list_matches += [''.join(matches)]
result = ', '.join(list_matches)
print(result)
