initial_int_input = list(map(int, input().split()))
command = input().split()

while command != ['end']:
    if command[0] == 'decrease':
        initial_int_input = list(x - 1 for x in initial_int_input)
    else:
        index1 = int(command[1])
        index2 = int(command[2])
        if command[0] == 'swap':
            initial_int_input[index1], initial_int_input[index2] = initial_int_input[index2], initial_int_input[index1]
        if command[0] == 'multiply':
            initial_int_input[index1] = initial_int_input[index1] * initial_int_input[index2]
    command = input().split()

result = ', '.join(str(number) for number in initial_int_input)
print(result)
