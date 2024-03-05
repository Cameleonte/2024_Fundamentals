user_text = input()

vowel_letters = ['a', 'o', 'u', 'e', 'i']
text_without_vowels = ''.join(letter for letter in user_text if letter.lower() not in vowel_letters)
print(text_without_vowels)
