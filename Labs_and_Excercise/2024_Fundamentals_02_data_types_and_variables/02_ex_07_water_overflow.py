pour_times = int(input())
tank_capacity = 255
total_water = 0
for time in range(pour_times):
    poured_water = int(input())
    if poured_water > tank_capacity - total_water:
        print('Insufficient capacity!')
        continue
    total_water += poured_water
print(total_water)
