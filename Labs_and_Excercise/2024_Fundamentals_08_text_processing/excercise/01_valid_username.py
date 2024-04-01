def valid_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def valid_characters(username):
    for symbol in username:
        if not (symbol.isalnum() or symbol == '-' or symbol == '_'):
            return False
    return True


def valid_redundant_symbols(username):
    if ' ' in username:
        return False
    return True


usernames = input().split(', ')
for text in usernames:
    if valid_length(text) and valid_characters(text) and valid_redundant_symbols(text):
        print(text)
