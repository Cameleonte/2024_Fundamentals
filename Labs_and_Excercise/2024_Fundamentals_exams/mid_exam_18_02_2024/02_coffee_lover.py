stock_coffees = input().split()
commands_number = int(input())

for num in range(1, commands_number + 1):
    command = input().split()
    if command[0] == 'Include':
        stock_coffees.append(command[1])
    if command[0] == 'Remove':
        if len(stock_coffees) <= int(command[2]):
            continue
        else:
            if command[1] == 'first':
                for i in range(int(command[2])):
                    stock_coffees.pop(0)
            elif command[1] == 'last':
                for i in range(int(command[2])):
                    stock_coffees.pop(-1)
    if command[0] == 'Prefer':
        if len(stock_coffees) <= int(command[1]) or len(stock_coffees) <= int(command[2]):
            continue
        else:
            stock_coffees[int(command[1])], stock_coffees[int(command[2])] =\
                stock_coffees[int(command[2])], stock_coffees[int(command[1])]
    if command[0] == 'Reverse':
        stock_coffees.reverse()

result = ' '.join(stock_coffees)
print(f'Coffees: \n{result}')
