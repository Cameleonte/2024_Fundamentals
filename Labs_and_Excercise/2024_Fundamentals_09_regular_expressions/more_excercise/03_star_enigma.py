import re


def decryption_message(current_decrypted_message):
    pattern = (r'\@([a-zA-Z]+)[^\@\,\-\,\!\:\>]*\:(\d+)[^\@\,\-\,\!\:\>]*'
               r'\!([AD])\![^\@\,\-\,\!\:\>]*\->(\d+)[^\@\,\-\,\!\:\>]*')
    #pattern = r'\@([a-zA-Z]+)([^\@\,\-\,\!\:\>])*\:(\d+)\2*\!([AD])\!\2*\->(\d+)\2*'
    result = re.findall(pattern, current_decrypted_message)
    if result:
        name, population, attack, soldiers = list(i for i in result[0])
        return name, population, attack, soldiers


def extract_key_and_transform(current_input):
    searched_letter = ['s', 't', 'a', 'r']
    key = 0
    for symbol in current_input.lower():
        if symbol in searched_letter:
            key += 1
    new_message = ''
    for element in current_input:
        current_symbol = ord(element) - key
        new_message += chr(current_symbol)
    return new_message


def printing_results(attack_count, destroy_count, attack_list, destroy_list):
    print(f'Attacked planets: {attack_count}')
    attack_list = sorted(attack_list)
    for planet in attack_list:
        print(f'-> {planet}')
    print(f'Destroyed planets: {destroy_count}')
    destroy_list = sorted(destroy_list)
    for planet in destroy_list:
        print(f'-> {planet}')


def main_function():
    messages_count = int(input())

    list_to_attack = []
    planets_to_attack = 0
    list_to_destroy = []
    planets_to_destroy = 0
    for message in range(messages_count):
        message_to_transform = input()
        message_to_decrypt = extract_key_and_transform(message_to_transform)
        if decryption_message(message_to_decrypt):
            planet_name, planet_population, attack_type, soldier_count = decryption_message(message_to_decrypt)
            if attack_type == 'A':
                list_to_attack.extend([planet_name])
                planets_to_attack += 1
            elif attack_type == 'D':
                list_to_destroy.extend([planet_name])
                planets_to_destroy += 1
    printing_results(planets_to_attack, planets_to_destroy, list_to_attack, list_to_destroy)


main_function()
