command = input()
tot_price_without_tax = 0
tot_price_parts = 0
taxes_amount = 0
taxes = 0.2
discount_special = 0.9
final_command = False

while True:
    part_price = 0
    current_tax = 0
    if command == 'special':
        tot_price_parts *= discount_special
        final_command = True
        break
    if command == 'regular':
        final_command = True
        break
    if float(command) < 0:
        print('Invalid price!')
        command = input()
        continue
    current_price = float(command)
    current_tax += current_price * taxes
    taxes_amount += current_tax
    tot_price_without_tax += current_price
    tot_price_parts += current_price + current_tax
    command = input()

if tot_price_parts == 0:
    print('Invalid order!')
if final_command and tot_price_parts != 0:
    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {tot_price_without_tax:.2f}$')
    print(f'Taxes: {taxes_amount:.2f}$')
    print('-----------')
    print(f'Total price: {tot_price_parts:.2f}$')
