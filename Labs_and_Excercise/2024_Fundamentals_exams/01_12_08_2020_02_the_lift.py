people_to_transport = int(input())
lift_state = input().split()
max_wagon_people = 4
loaded_lift_state = []
lift_full = False

for wagon in lift_state:
    people_in_wagon = int(wagon)
    if people_in_wagon == 4:
        loaded_lift_state.append(people_in_wagon)
        if int(lift_state[-1]) == 4:
            lift_full = True
        continue
    if people_in_wagon < 4:
        wagon_free_space = max_wagon_people - people_in_wagon
        if people_to_transport >= wagon_free_space:
            people_to_transport -= wagon_free_space
        else:
            wagon_free_space = people_to_transport
            people_to_transport = 0
        tot_people_in_wagon = people_in_wagon + wagon_free_space
        loaded_lift_state.append(tot_people_in_wagon)
if int(loaded_lift_state[-1]) == 4:
    lift_full = True

if people_to_transport > 0:
    print(f'There isn\'t enough space! {people_to_transport} people in a queue!')
    print(*loaded_lift_state)

if people_to_transport == 0 and not lift_full:
    print('The lift has empty spots!')
    print(*loaded_lift_state)

if people_to_transport == 0 and lift_full:
    print(*loaded_lift_state)
