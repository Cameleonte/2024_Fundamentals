country_list = input().split(', ')
capitals_list = input().split(', ')

dicty = dict(zip(country_list, capitals_list))
for key, value in dicty.items():
    print(f'{key} -> {value}')
