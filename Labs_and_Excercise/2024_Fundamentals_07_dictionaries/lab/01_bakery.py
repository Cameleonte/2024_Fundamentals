some_list = input().split()

dict_products = {}
for elem in range(0, len(some_list), 2):
    quantity = int(some_list[elem + 1])
    product = some_list[elem]
    dict_products[product] = quantity
print(dict_products)
