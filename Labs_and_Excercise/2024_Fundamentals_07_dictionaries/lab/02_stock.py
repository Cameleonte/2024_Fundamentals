products = input().split()
requested_products = input().split()

dictionary_products = {}
for item in range(0, len(products), 2):
    product = products[item]
    quantity = int(products[item + 1])
    dictionary_products[product] = quantity
for request_product in requested_products:
    if request_product in dictionary_products.keys():
        quantity = int(dictionary_products[request_product])
        print(f'We have {quantity} of {request_product} left')
    else:
        print(f'Sorry, we don\'t have {request_product}')
