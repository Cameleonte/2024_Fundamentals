def shooting_targets(targets):
    target_shot = 0
    while True:
        command = input()
        new_list = []
        if command == "End":
            result = ' '.join(map(str, targets))
            print(f"Shot targets: {target_shot} -> {result}")
            break
        if 0 <= int(command) < len(targets):
            if targets[int(command)] != -1:
                for num in targets:
                    if num == -1:
                        new_list.append(num)
                    if num != - 1 and num <= targets[int(command)]:
                        num += targets[int(command)]
                        new_list.append(num)
                    elif num != - 1 and num > targets[int(command)]:
                        num -= targets[int(command)]
                        new_list.append(num)
                new_list[int(command)] = -1
                target_shot += 1
                targets = new_list
        else:
            continue


my_sequence = list(map(int, input().split(' ')))
shooting_targets(my_sequence)
