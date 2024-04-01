some_strings = input().split()
result = ''

for string in some_strings:
    result += len(string) * string
print(result)
