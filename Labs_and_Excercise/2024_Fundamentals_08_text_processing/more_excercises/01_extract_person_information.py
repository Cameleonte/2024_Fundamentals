def extracting_name(phrase):
    for index in range(len(phrase)):
        element = phrase[index]
        if '@' in element:
            name = ''
            for symbol in element[element.index('@') + 1:]:
                if symbol == '|':
                    break
                name += symbol
            return name


def extracting_age(phrase):
    for index in range(len(phrase)):
        element = phrase[index]
        if '#' in element:
            age = ''
            for symbol in element[element.index('#') + 1:]:
                if symbol == '*':
                    break
                age += symbol
            return age


lines_number = int(input())

for line in range(lines_number):
    text = input().split()
    someones_name = extracting_name(text)
    his_age = extracting_age(text)
    print(f'{someones_name} is {his_age} years old.')
