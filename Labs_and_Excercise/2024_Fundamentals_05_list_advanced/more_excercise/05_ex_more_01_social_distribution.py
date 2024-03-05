
def distribution(citizens, poorest_value, no_action):
    no_action = False
    for value in citizens:
        max_value = max(citizens)
        min_value = min(citizens)
        additional_value = poorest_value - min_value
        if max_value - poorest_value >= additional_value:
            if value < poorest_value:
                min_position = citizens.index(min_value)
                max_position = citizens.index(max_value)
                citizens.pop(min_position)
                citizens.insert(min_position, poorest_value)
                citizens.pop(max_position)
                citizens.insert(max_position, max_value - additional_value)

        else:
            print('No equal distribution possible')
            no_action = True
            break
    return citizens, no_action


population = list(map(int, input().split(', ')))
min_wealth = int(input())
nothing_to_distribute = False
population, nothing_to_distribute = distribution(population, min_wealth, nothing_to_distribute)
if not nothing_to_distribute:
    print(population)
