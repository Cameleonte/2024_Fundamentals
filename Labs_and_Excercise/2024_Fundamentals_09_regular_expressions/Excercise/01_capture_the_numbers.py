import re

user_input = input()
while user_input:
    pattern = '\d+'
    result = re.findall(pattern, user_input)
    if result:
        res_to_print = ' '.join(result)
        print(res_to_print, end=' ')
    user_input = input()
