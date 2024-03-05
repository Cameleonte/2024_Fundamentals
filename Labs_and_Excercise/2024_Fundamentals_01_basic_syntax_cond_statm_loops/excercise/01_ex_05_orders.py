received_orders = int(input())
price = 0
total_price = 0

for order in range(1, received_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        price = price_per_capsule * capsules_per_day * days
        total_price += price
        print(f'The price for the coffee is: ${price:.2f}')
    else:
        continue

print(f'Total: ${total_price:.2f}')
