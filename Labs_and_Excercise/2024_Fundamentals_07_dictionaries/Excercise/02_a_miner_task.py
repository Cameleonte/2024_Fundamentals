resource_diction = {}

while True:
    resource = input()

    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in resource_diction:
        resource_diction[resource] = 0
    resource_diction[resource] += quantity
for key, value in resource_diction.items():
    print(f'{key} -> {value}')
