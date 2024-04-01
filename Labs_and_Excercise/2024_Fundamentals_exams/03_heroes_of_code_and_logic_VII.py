def spelling(data, dictionary1):
    unused_action, hero_name, mp_needed, spell_name = data.split(' - ')
    current_mp = dictionary1[hero_name][1]
    if int(mp_needed) > current_mp:
        print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    else:
        current_mp -= int(mp_needed)
        dictionary1[hero_name] = [dictionary1[hero_name][0], current_mp]
        print(f'{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!')
    return dictionary1


def damage(data, dictionary2):
    unused_action, hero_name, damage_received, attacker = data.split(' - ')
    current_hp = dictionary2[hero_name][0]
    if int(damage_received) >= current_hp:
        del dictionary2[hero_name]
        print(f'{hero_name} has been killed by {attacker}!')
    else:
        current_hp -= int(damage_received)
        dictionary2[hero_name] = [current_hp, dictionary2[hero_name][1]]
        print(f'{hero_name} was hit for {damage_received} HP by {attacker} and now has {current_hp} HP left!')
    return dictionary2


def re_charge(data, dictionary3):
    unused_action, hero_name, amount = data.split(' - ')
    current_mp = dictionary3[hero_name][1]
    new_mp = current_mp + int(amount)
    if new_mp > 200:
        new_mp = 200
        amount = new_mp - current_mp
    print(f'{hero_name} recharged for {amount} MP!')
    dictionary3[hero_name] = [dictionary3[hero_name][0], new_mp]
    return dictionary3


def heal(data, dictionary):
    unused_action, hero_name, amount = data.split(' - ')
    current_hp = dictionary[hero_name][0]
    new_hp = current_hp + int(amount)
    if new_hp > 100:
        new_hp = 100
        amount = new_hp - current_hp
    print(f'{hero_name} healed for {amount} HP!')
    dictionary[hero_name] = [new_hp, dictionary[hero_name][1]]
    return dictionary


def initialize(heroes):
    heroes_dictionary = {}
    for hero in range(heroes):
        hero_name, hero_hp, hero_mp = input().split()
        heroes_dictionary[hero_name] = [int(hero_hp), int(hero_mp)]
    command = input()
    while command != 'End':
        action = command.split(' - ')[0]
        if action == 'CastSpell':
            heroes_dictionary = spelling(command, heroes_dictionary)
        elif action == 'TakeDamage':
            heroes_dictionary = damage(command, heroes_dictionary)
        elif action == 'Recharge':
            heroes_dictionary = re_charge(command, heroes_dictionary)
        elif action == 'Heal':
            heroes_dictionary = heal(command, heroes_dictionary)
        command = input()
    return heroes_dictionary


heroes_number = int(input())
new_dictionary = initialize(heroes_number)
for hero_left in new_dictionary:
    name = hero_left
    hp = new_dictionary[name][0]
    mp = new_dictionary[name][1]
    print(f'{name}\n  HP: {hp}\n  MP: {mp}')
