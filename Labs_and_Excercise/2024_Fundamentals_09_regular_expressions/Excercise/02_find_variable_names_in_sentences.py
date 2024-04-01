import re

single_string = input()
pattern = r'\b_([a-zA-Z0-9]+)\b'
result = re.findall(pattern, single_string)
print(','.join(result))
