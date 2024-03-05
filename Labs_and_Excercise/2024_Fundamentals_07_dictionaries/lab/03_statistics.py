products_dict = {}

receiving_products = input().split(': ')

while receiving_products[0] != 'statistics':
    product = receiving_products[0]
    quantity = int(receiving_products[1])
    if product in products_dict.keys():
        products_dict[product] += quantity
    else:
        products_dict[product] = quantity
    receiving_products = input().split(': ')
print('Products in stock:')
for product in products_dict.keys():
    print(f'- {product}: {products_dict[product]}')
print(f'Total Products: {len(products_dict)}\nTotal Quantity: {sum(products_dict.values())}')
