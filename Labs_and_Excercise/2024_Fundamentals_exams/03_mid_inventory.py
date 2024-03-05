def check_items(objects):
    return command[1] if command[1] in objects else False


def collect_items(objects):
    if not check_items(objects):
        objects.append(command[1])
    return objects


def drop_items(objects):
    if check_items(objects):
        objects.remove(command[1])
    return objects


def combine_items(objects):
    combine_objects = command[1].split(':')
    if combine_objects[0] in objects:
        old_item_index = objects.index(combine_objects[0])
        objects.insert(old_item_index + 1, combine_objects[1])
    return objects


def renew_items(objects):
    if check_items(objects):
        objects.remove(command[1])
        objects.append(command[1])
    return objects


items = input().split(', ')
while True:
    command = input().split(' - ')
    if command[0] == 'Craft!':
        print(', '.join(map(str, items)))
        break

    elif command[0] == 'Collect':
        collect_items(items)
    elif command[0] == 'Drop':
        drop_items(items)
    elif command[0] == 'Combine Items':
        combine_items(items)
    elif command[0] == 'Renew':
        renew_items(items)
