import re

strings = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
iterable = re.finditer(pattern, strings)

for el in iterable:
    print(el.group(), end=' ')
