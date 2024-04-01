import re

given_string = input()

pattern = r'[@|#]+([a-z]{3,})[@|#]+[^a-zA-Z0-9]*(\/+)(\d+)\2'
list_info = re.findall(pattern, given_string)

if list_info:
    for item in list_info:
        amount = item[2]
        color = item[0]
        print(f'You found {amount} {color} eggs!')
