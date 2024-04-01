morse_words = input().split(' | ')
morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

message = ''
for word in morse_words:
    morse_letter_list = word.split()
    for letter in morse_letter_list:
        if letter in morse_code_dict.values():
            english_letter = list(morse_code_dict.keys())[list(morse_code_dict.values()).index(letter)]
            message += english_letter
    message += ' '
print(message)
