def check_info(plant_info_dict, current_input):
    item = current_input.split(' - ')[0]
    if item in plant_info_dict.keys():
        return True
    else:
        print('error')


def rate_func(mydict, insertion):
    plant, rate = insertion.split(' - ')
    mydict[plant]['Rating'].append(rate)


def update_func(mydict, insertion):
    plant, new_rarity = insertion.split(' - ')
    mydict[plant]['Rarity'] = new_rarity


def reset_func(mydict, insertion):
    plant = insertion
    mydict[plant]['Rating'].clear()


def printing_function(mydict):
    print('Plants for the exhibition:')
    for plant in mydict:
        rarity = mydict[plant]['Rarity']
        rating_list = mydict[plant]['Rating']
        if not rating_list:
            average_rating = 0
        else:
            int_values_rating = [int(a) for a in rating_list]
            average_rating = sum(int_values_rating) / len(int_values_rating)
        print(f'- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}')


def main_action(info):
    plant_dictionary = {}
    for current_plant in range(info):
        plant, rarity = input().split('<->')
        plant_dictionary[plant] = dict(Rarity=rarity, Rating=[])

    while True:
        command = input()
        if command == 'Exhibition':
            return plant_dictionary
        action, current_info = command.split(': ')
        if check_info(plant_dictionary, current_info):
            if action == 'Rate':
                rate_func(plant_dictionary, current_info)
            elif action == 'Update':
                update_func(plant_dictionary, current_info)
            elif action == 'Reset':
                reset_func(plant_dictionary, current_info)
        else:
            continue


info_lines = int(input())
info_dict = main_action(info_lines)
printing_function(info_dict)
