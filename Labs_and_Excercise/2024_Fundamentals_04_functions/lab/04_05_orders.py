def order_price(product, quantity):
    price = 0
    if product == 'coffee':
        price = 1.50 * quantity
    elif product == 'water':
        price = 1.00 * quantity
    elif product == 'coke':
        price = 1.40 * quantity
    elif product == 'snacks':
        price = 2.00 * quantity
    return price


user_product = input()
user_quantity = int(input())
result = order_price(user_product, user_quantity)
print(f'{result:.2f}')
