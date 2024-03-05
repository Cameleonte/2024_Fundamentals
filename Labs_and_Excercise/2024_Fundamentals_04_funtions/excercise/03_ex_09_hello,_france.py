items_and_prices = input().split('|')
budget = float(input())

france_ticket = 150
markup = 0.4
max_price_clothes = 50.00
max_price_shoes = 35.00
max_price_accessories = 20.50
new_prices_list = []
for item in items_and_prices:
    item_type, item_price = item.split('->')
    item_price = float(item_price)
    item_new_price = 0
    if (item_type == 'Clothes' and 0 < item_price <= max_price_clothes) or \
       (item_type == 'Shoes' and 0 < item_price <= max_price_shoes) or \
       (item_type == 'Accessories' and 0 < item_price <= max_price_accessories):
        if item_price <= budget:
            budget -= item_price
            item_new_price = round(1.4 * item_price, 2)
            new_prices_list.append(item_new_price)
print(*new_prices_list, sep=' ')
print(f'Profit: {((sum(new_prices_list) * 0.4) / 1.4):.2f}')
if sum(new_prices_list) + budget >= france_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')

'''Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
90
'''