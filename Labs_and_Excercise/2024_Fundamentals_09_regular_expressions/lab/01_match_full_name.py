import re

names = input()
pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"
result = re.findall(pattern, names)
print(' '.join(result))
