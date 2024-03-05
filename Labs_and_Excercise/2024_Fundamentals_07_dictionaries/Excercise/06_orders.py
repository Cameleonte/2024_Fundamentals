from functools import reduce

product_dictionary = {}
prod_price_dict = {}
total_price = 0

while True:
    products_data = input()
    if products_data == 'buy':
        break

    product_name, product_price, product_quantity = products_data.split()
    if product_name not in product_dictionary:
        product_dictionary[product_name] = [float(product_price), int(product_quantity)]
    else:
        product_dictionary[product_name][0] = float(product_price)
        product_dictionary[product_name][1] += int(product_quantity)
    total_price = reduce((lambda x, y: x * y), product_dictionary[product_name])
    prod_price_dict[product_name] = total_price

for product in prod_price_dict:
    print(f"{product} -> {prod_price_dict[product]:.2f}")



