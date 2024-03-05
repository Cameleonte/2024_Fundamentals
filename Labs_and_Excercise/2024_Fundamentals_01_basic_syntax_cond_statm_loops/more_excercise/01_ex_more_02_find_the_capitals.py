user_input = input()

upper_case_letters_list = []
for symbol in range(len(user_input)):
    if user_input[symbol].isalpha() and user_input[symbol].isupper():
        upper_case_letters_list.append(symbol)
print(upper_case_letters_list)
