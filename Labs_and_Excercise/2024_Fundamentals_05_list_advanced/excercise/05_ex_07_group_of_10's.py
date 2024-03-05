def filtered_numbers(number_sequence):
    boundary = 10
    while True:
        list_of_numbers = list(x for x in number_sequence if x <= boundary)
        number_sequence = list(filter(lambda x: x in number_sequence if x > boundary else x == 0, number_sequence))
        print(f'Group of {boundary}\'s: {list_of_numbers}')
        boundary += 10
        if not number_sequence:
            break


input_numbers = list(map(int, input().split(', ')))
filtered_numbers(input_numbers)
