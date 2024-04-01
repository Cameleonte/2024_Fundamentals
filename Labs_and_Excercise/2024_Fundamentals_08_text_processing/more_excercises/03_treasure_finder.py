def extracting_info(decrypted_text):
    treasure_type = ''
    coordinates = ''
    treasure_type_char_position = decrypted_text.find('&')
    next_type_char_position = decrypted_text.find('&', (decrypted_text.index('&') + 1))
    treasure_type = decrypted_text[treasure_type_char_position + 1: next_type_char_position]
    coordinates_char_position = decrypted_text.find('<')
    next_coordinates_char_position = decrypted_text.find('<', (decrypted_text.index('>') + 1))
    coordinates = decrypted_text[coordinates_char_position + 1: next_coordinates_char_position]
    return treasure_type, coordinates


def looping(some_string):
    key_index = 0
    phrase = ''
    for current_index in range(len(some_string)):
        current_letter = ord(some_string[current_index]) - keys[key_index]
        phrase += chr(current_letter)
        key_index += 1
        if key_index == len(keys):
            key_index = 0
    return phrase


keys = list(map(int, input().split()))

while True:
    current_string = input()
    if current_string == 'find':
        break
    result = looping(current_string)
    treasure, details = extracting_info(result)

    print(f'Found {treasure} at {details}')
