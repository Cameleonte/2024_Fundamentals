adventure_days = int(input())
players_number = int(input())
groups_energy = float(input())
water_per_day_for_person = float(input())
food_per_day_for_person = float(input())

tot_water = water_per_day_for_person * adventure_days * players_number
tot_food = food_per_day_for_person * adventure_days * players_number
enough_energy = False
current_energy = groups_energy


for day in range(1, adventure_days + 1):
    energy_loss = float(input())
    if current_energy <= energy_loss:
        print(f'You will run out of energy. You will be left with {tot_food:.2f} food and {tot_water:.2f} water.')
        break
    current_energy = current_energy - energy_loss
    if day % 2 == 0:
        current_energy += 0.05 * current_energy
        tot_water -= 0.3 * tot_water
    if day % 3 == 0:
        current_energy += 0.1 * current_energy
        tot_food -= tot_food / players_number
    if day == adventure_days:
        enough_energy = True
        break

if enough_energy:
    print(f'You are ready for the quest. You will be left with - {current_energy:.2f} energy!')
