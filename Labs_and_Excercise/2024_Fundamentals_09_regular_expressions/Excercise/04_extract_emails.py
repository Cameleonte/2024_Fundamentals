import re

single_string = input()
pattern = r'\s(([a-z0-9]+)[a-z0-9\.\-\_]*@([a-z0-9\-]+(\.[a-z]+)+))\b'
result = re.findall(pattern, single_string)
for elem in result:
    print(elem[0])
