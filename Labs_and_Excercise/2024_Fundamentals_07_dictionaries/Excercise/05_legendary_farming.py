materials_dictionary = {}
legendary_items_list = ['Shadowmourne', 'Valanyr', 'Dragonwrath']
key_materials = ['shards', 'fragments', 'motes']
legendary_dict = dict(zip(key_materials, legendary_items_list))

item_obtained = False
while not item_obtained:
    materials_gathered = input().split()
    for value in range(0, len(materials_gathered), 2):
        quantity = int(materials_gathered[value])
        material = (materials_gathered[value + 1]).lower()
        if material not in materials_dictionary:
            materials_dictionary[material] = 0
        materials_dictionary[material] += quantity
        for item in materials_dictionary:
            if materials_dictionary[item] >= 250 and item in key_materials:
                print(f"{legendary_dict[item]} obtained!")
                materials_dictionary[item] -= 250
                item_obtained = True
                break
        if item_obtained:
            break

for key_mat in key_materials:
    if key_mat not in materials_dictionary:
        materials_dictionary[key_mat] = 0
    print(f'{key_mat}: {materials_dictionary[key_mat]}')
    del materials_dictionary[key_mat]
if materials_dictionary is not None:
    for junk in materials_dictionary:
        print(f'{junk}: {materials_dictionary[junk]}')
