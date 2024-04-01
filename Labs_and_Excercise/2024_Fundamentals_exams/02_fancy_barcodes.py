import re

input_number = int(input())
for num in range(input_number):
    characters = input()
    pattern = r'[@][#]+([A-Z][a-z0-9A-Z]{4,}[A-Z])[@][#]+'
    new_sequence = re.findall(pattern, characters)
    if new_sequence:
        product_group = ''.join(d for d in new_sequence[0] if d.isdigit())
        if not product_group:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
