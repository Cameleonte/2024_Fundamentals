def check_empty_space_or_kate(string):
    x = 0
    # for x in range(len(string)):
    #     if string[x] == 'k':
    #         k_position = x
    k_position = list(x for x in range(len(string) if string[x] == 'k' else 0))
    return k_position


mazes_rows = int(input())
while True:
    row = input()
    kates_position = check_empty_space_or_kate(row)
    print(kates_position)
