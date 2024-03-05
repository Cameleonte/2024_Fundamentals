cells_info = input().split('#')
water_amount = int(input())

effort_value = 0
total_fire = 0
print('Cells:')
for cell in cells_info:
    current_cell_info = cell.split(' = ')
    if (current_cell_info[0] == 'High' and 81 <= int(current_cell_info[1]) <= 125) or \
       (current_cell_info[0] == 'Medium' and 51 <= int(current_cell_info[1]) <= 80) or \
       (current_cell_info[0] == 'Low' and 1 <= int(current_cell_info[1]) <= 50):
        if 0 < int(current_cell_info[1]) <= water_amount:
            water_amount -= int(current_cell_info[1])
            effort_value += 0.25 * int(current_cell_info[1])
            print(f' - {int(current_cell_info[1])}')
            total_fire += int(current_cell_info[1])
print(f'Effort: {effort_value:.2f}')
print(f'Total Fire: {total_fire}')
