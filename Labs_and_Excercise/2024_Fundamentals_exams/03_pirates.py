def city_list_planing():
    cities_dictionary = {}
    city_data = input().split('||')
    while True:
        city = city_data[0]
        if city == 'Sail':
            break
        population, gold = int(city_data[1]), int(city_data[2])
        if city not in cities_dictionary:
            cities_dictionary[city] = {'Population': population, 'Gold': gold}
        else:
            cities_dictionary[city]['Population'] += population
            cities_dictionary[city]['Gold'] += gold
        city_data = input().split('||')
    return cities_dictionary


def events(city_dict):
    text = input().split('=>')
    while True:
        event = text[0]
        if event == 'End':
            break
        town = text[1]
        if event == 'Plunder':
            population, gold = int(text[2]), int(text[3])
            city_dict[town]['Population'] -= population
            city_dict[town]['Gold'] -= gold
            print(f'{town} plundered! {gold} gold stolen, {population} citizens killed.')
            if city_dict[town]['Population'] <= 0 or city_dict[town]['Gold'] <= 0:
                del city_dict[town]
                print(f'{town} has been wiped off the map!')
        elif event == 'Prosper':
            gold = int(text[2])
            if gold < 0:
                print('Gold added cannot be a negative number!')
            else:
                city_dict[town]['Gold'] += gold
                tot_gold = city_dict[town]['Gold']
                print(f'{gold} gold added to the city treasury. {town} now has {tot_gold} gold.')
        text = input().split('=>')
    return city_dict


dictionary = city_list_planing()
dictionary = events(dictionary)
if len(dictionary) != 0:
    print(f'Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:')
    for town in dictionary.keys():
        people = dictionary[town]['Population']
        gold = dictionary[town]['Gold']
        print(f'{town} -> Population: {people} citizens, Gold: {gold} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
