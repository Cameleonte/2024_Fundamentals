decorations_quantity = int(input())
days_to_christmas = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
tot_price = 0
christmas_spirit = 0

for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        decorations_quantity += 2
    if day % 2 == 0:
        tot_price += ornament_set_price * decorations_quantity
        christmas_spirit += 5
    if day % 3 == 0:
        tot_price += tree_skirt_price * decorations_quantity + tree_garland_price * decorations_quantity
        christmas_spirit += 3 + 10
    if day % 5 == 0:
        tot_price += tree_lights_price * decorations_quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        tot_price += tree_skirt_price + tree_lights_price + tree_garland_price
if days_to_christmas % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {tot_price}')
print(f'Total spirit: {christmas_spirit}')
