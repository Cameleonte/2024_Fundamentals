initial_deck = input().split()
faro_shuffle_count = int(input())

for shuffle in range(1, faro_shuffle_count + 1):
    len_half = int(len(initial_deck) / 2)
    first_half = initial_deck[:len_half]
    second_half = initial_deck[len_half:]
    new_list = []
    for index in range(len_half):
        new_list.append(first_half[index])
        new_list.append(second_half[index])
    initial_deck = new_list

print(initial_deck)
