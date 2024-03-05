initial_energy = int(input())
battle_count = 0

while True:
    command = input()
    if command == 'End of battle':
        print(f'Won battles: {battle_count}. Energy left: {initial_energy}')
        break
    if initial_energy < int(command):
        print(f'Not enough energy! Game ends with {battle_count} won battles and {initial_energy} energy')
        break
    initial_energy -= int(command)
    battle_count += 1
    if battle_count % 3 == 0:
        initial_energy += battle_count
