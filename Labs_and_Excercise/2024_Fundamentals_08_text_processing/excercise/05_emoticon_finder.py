user_text = input()

for char in range(len(user_text)):
    if user_text[char] == ':':
        print(f':{user_text[char + 1]}')
