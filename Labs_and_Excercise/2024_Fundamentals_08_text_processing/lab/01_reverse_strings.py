while True:
    text = input()
    if text == 'end':
        break
    reversed_text = ''
    for letter in range(len(text) - 1, -1, -1):  # in reversed(text)
        reversed_text += text[letter]
    print(f'{text} = {reversed_text}')
