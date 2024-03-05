budget = int(input())

command = input()

while command != 'End':
    product_price = float(command)
    budget -= product_price
    if budget < 0:
        print('You went in overdraft!')
        break
    command = input()
else:
    print('You bought everything needed.')
