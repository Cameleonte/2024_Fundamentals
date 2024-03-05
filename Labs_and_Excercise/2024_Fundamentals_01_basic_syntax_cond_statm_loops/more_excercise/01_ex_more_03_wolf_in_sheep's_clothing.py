animal_specie = input()
animal_specie_list = (animal_specie.split(', '))
'''string_formed = ''
animal_specie_list = []
digit_met = False

for digits in animal_specie:
    if digits == 's':
        animal_specie_list.append('sheep')
    if digits == 'w':
        animal_specie_list.append('wolf')'''
if animal_specie_list[-1:] == ['wolf']:
    print('Please go away and stop eating my sheep')
else:
    new_list = animal_specie_list[animal_specie_list.index('wolf'):]
    digits = len(new_list)
    sheep_in_danger = digits - 1
    print(f'Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!')
