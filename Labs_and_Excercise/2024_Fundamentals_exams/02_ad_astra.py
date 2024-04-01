import re
from math import floor
string = input()

pattern1 = r"([#|])([a-zA-Z\s]+)\1([0-9][0-9]/[0-9][0-9]/[0-9][0-9])\1([0-9]+)\1"
list_result = re.findall(pattern1, string)
tot_calories = 0

first_printed = False
to_print = ''
for element in range(len(list_result)):
    item_name, exp_date, calories = list_result[element][1], list_result[element][2], list_result[element][3]
    tot_calories += int(calories)
    to_print += f'Item: {item_name}, Best before: {exp_date}, Nutrition: {calories}\n'
days_to_eat = floor(tot_calories / 2000)
print(f'You have food to last you for: {days_to_eat} days!')
print(to_print)
