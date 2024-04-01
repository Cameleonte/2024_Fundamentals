import re

while True:
    text = input()
    if not text:
        break
    pattern = r"(w{3}\.[a-zA-Z0-9\-\.]+\.([a-z]+))"
    result = re.search(pattern, text)
    if result:
        print(result.group(1))
