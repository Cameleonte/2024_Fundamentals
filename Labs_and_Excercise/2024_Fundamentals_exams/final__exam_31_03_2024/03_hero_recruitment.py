# command = input()
# heroes_collection = {}
#
# while command != "End":
#     action, hero_name = command.split()[0], command.split()[1]
#
#     if action == 'Enroll':
#         if hero_name in heroes_collection:
#             print(f'{hero_name} is already enrolled.')
#         else:
#             heroes_collection[hero_name] = []
#     elif action == 'Learn':
#         spell_name = command.split()[2]
#         if hero_name in heroes_collection:
#             if spell_name not in heroes_collection[hero_name]:
#                 heroes_collection[hero_name].append(spell_name)
#             else:
#                 print(f'{hero_name} has already learnt {spell_name}.')
#         else:
#             print(f"{hero_name} doesn't exist.")
#     elif action == 'Unlearn':
#         spell_name = command.split()[2]
#         if hero_name in heroes_collection:
#             if spell_name in heroes_collection[hero_name]:
#                 heroes_collection[hero_name].remove(spell_name)
#             else:
#                 print(f"{hero_name} doesn't know {spell_name}.")
#         else:
#             print(f"{hero_name} doesn't exist.")
#     command = input()
#
# print('Heroes:')
#
# for hero in heroes_collection:
#     if heroes_collection[hero]:
#         for spell in heroes_collection[hero]:
#             if heroes_collection[hero].index(spell) == len(heroes_collection[hero]) - 1:
#                 print(f'== {hero}: {spell}')
#             else:
#                 print(f'=={hero}: {spell}', end=', ')
#     else:
#         print(f'== {hero}:')


def enroll_heroes(hero_name, collection):
    hero_name = hero_name.split()[1]
    if hero_name not in collection:
        collection[hero_name] = []
    else:
        print(f"{hero_name} is already enrolled.")
    return collection


def learn_unlearn_spell(info, collection):
    action, hero_name, spell_name = info.split()[0], info.split()[1], info.split()[2]
    if hero_name in collection:

        if action == "Learn":
            if spell_name not in collection[hero_name]:
                collection[hero_name].append(spell_name)
            else:
                print(f"{hero_name} has already learnt {spell_name}.")

        elif action == "Unlearn":
            if spell_name in collection[hero_name]:
                collection[hero_name].remove(spell_name)
        else:
            print(f"{hero_name} doesn't know {spell_name}.")

    else:
        print(f"{hero_name} doesn't exist.")
    return collection


def main_function(init_input, heroes_collection):
    action = init_input.split()[0]
    if action == "Enroll":
        heroes_collection = enroll_heroes(init_input, heroes_collection)
    else:
        heroes_collection = learn_unlearn_spell(init_input, heroes_collection)
    return heroes_collection


command = input()
heroes_data = {}

while command != "End":
    main_function(command, heroes_data)

    command = input()

print('Heroes:', end='')
if heroes_data:
    for hero in heroes_data:
        print(f'\n== {hero}: ', end='')
        if heroes_data[hero]:
            print(', '.join(heroes_data[hero]), end='')
