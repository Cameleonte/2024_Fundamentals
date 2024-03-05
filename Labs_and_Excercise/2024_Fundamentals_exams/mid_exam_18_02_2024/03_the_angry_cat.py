price_ratings = list(map(int, input().split(', ')))
entry_point = int(input())
type_to_break = input()

left_list = price_ratings[:entry_point]
right_list = price_ratings[(entry_point + 1):]
damage_value = price_ratings[entry_point]
right_sum = 0
left_sum = 0
position = ''
if type_to_break == 'cheap':
    left_value_to_add = [x for x in left_list if x < damage_value]
    left_sum = sum(left_value_to_add)
    right_value_to_add = [x for x in right_list if x < damage_value]
    right_sum = sum(right_value_to_add)
elif type_to_break == 'expensive':
    left_value_to_add = [x for x in left_list if x >= damage_value]
    left_sum = sum(left_value_to_add)
    right_value_to_add = [x for x in right_list if x >= damage_value]
    right_sum = sum(right_value_to_add)
if right_sum <= left_sum:
    position = 'Left'
    print(f'{position} - {left_sum}')
else:
    position = 'Right'
    print(f'{position} - {right_sum}')
