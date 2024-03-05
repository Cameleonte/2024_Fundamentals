def center_rooms():
    total_free_chairs = 0
    current_room = 1
    while True:
        if current_room > rooms_count:
            break

        chair_number, visitors = input().split()

        if len(chair_number) < int(visitors):
            needed_chairs_in_room = len(chair_number) - int(visitors)

            if needed_chairs_in_room < 0:
                print(f'{abs(needed_chairs_in_room)} more chairs needed in room {current_room}')
                total_free_chairs -= abs(needed_chairs_in_room)
        else:
            total_free_chairs += (len(chair_number) - int(visitors))
        current_room += 1
    if total_free_chairs >= 0:
        print(f'Game On, {total_free_chairs} free chairs left')


rooms_count = int(input())
center_rooms()

'''def check_the_rooms(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
        free_chairs += difference
    return free_chairs
 
count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")'''