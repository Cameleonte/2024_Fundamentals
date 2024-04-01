import re

user_input = input()
print('Bought furniture:')
tot_price = 0
while user_input != 'Purchase':
    pattern = r'>>(\w+)<<(\d+\.*\d+)!(\d+)\b'
    list_products = re.findall(pattern, user_input)
    if list_products:
        for element in list_products:
            product, price, number = element[0], element[1], element[2]
            tot_price += float(price) * int(number)
            print(f'{product}')
    user_input = input()
print(f'Total money spend: {tot_price:.2f}')
