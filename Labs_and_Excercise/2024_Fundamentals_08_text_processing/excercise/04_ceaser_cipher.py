random_text = input()
encrypted_text = ''

for char in random_text:
    new_char_number = ord(char) + 3
    new_char = chr(new_char_number)
    encrypted_text += new_char
print(encrypted_text)
