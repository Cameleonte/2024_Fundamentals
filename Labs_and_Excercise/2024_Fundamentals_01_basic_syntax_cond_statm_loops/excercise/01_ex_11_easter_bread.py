budget = float(input())
one_kg_flour_price = float(input())
one_pack_eggs_price = 0.75 * one_kg_flour_price
one_lt_milk_price = 1.25 * one_kg_flour_price
one_bread_price = one_kg_flour_price + one_pack_eggs_price + 0.25 * one_lt_milk_price
colored_eggs_collected = 0
current_bread_count = 0

while True:
    if budget <= one_bread_price:
        break
    budget -= one_bread_price
    current_bread_count += 1
    colored_eggs_collected += 3
    if current_bread_count % 3 == 0:
        if colored_eggs_collected < (current_bread_count - 2):
            break
        colored_eggs_collected -= (current_bread_count - 2)
print(f'You made {current_bread_count} loaves of Easter bread!'
      f' Now you have {colored_eggs_collected} eggs and {budget:.2f}BGN left.')
