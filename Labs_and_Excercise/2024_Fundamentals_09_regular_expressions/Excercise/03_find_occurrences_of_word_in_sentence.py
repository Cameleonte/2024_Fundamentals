import re

sentence = input()
word = input()
pattern = fr'\b{word}\b'
matches = re.findall(pattern, sentence, re.IGNORECASE)
print(len(matches))
