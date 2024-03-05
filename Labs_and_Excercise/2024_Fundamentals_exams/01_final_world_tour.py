def check_index(index):
    return 0 <= index < len(init_travel_stops)


def add_stop(action, result):
    idx = int(action[1])
    if check_index(idx):
        result = result[:idx] + action[2] + result[idx:]
    return result


def rem_stop(action, result):
    idx1, idx2 = int(action[1]), int(action[2])
    if check_index(idx1) and check_index(idx2):
        result = result[:idx1] + result[idx2 + 1:]
    return result


def switch(action, result):
    if action[1] in init_travel_stops:
        result = result.replace(action[1], action[2])
    return result


init_travel_stops = input()

while True:
    command = input().split(':')
    if command[0] == "Travel":
        print(f'Ready for world tour! Planned stops: {init_travel_stops}')
        break

    if command[0] == 'Add Stop':
        init_travel_stops = add_stop(command, init_travel_stops)
    elif command[0] == 'Remove Stop':
        init_travel_stops = rem_stop(command, init_travel_stops)
    elif command[0] == 'Switch':
        init_travel_stops = switch(command, init_travel_stops)
    print(init_travel_stops)
