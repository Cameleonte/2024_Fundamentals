snowballs_number = int(input())
max_weight = 0
max_quality = 0
max_value = 0
max_time = 0

for ball in range(snowballs_number):
    snowball_weight = int(input())
    time_to_target = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / time_to_target) ** snowball_quality
    if snowball_value > max_value:
        max_weight = snowball_weight
        max_quality = snowball_quality
        max_value = int(snowball_value)
        max_time = time_to_target

print(f'{max_weight} : {max_time} = {max_value} ({max_quality})')
