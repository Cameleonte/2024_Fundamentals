number_sequence = input().split()

finish = len(number_sequence) // 2
tot_seconds_left = 0
tot_seconds_right = 0
for sec_left in number_sequence[:finish]:
    if sec_left == '0':
        tot_seconds_left *= 0.8
    tot_seconds_left += int(sec_left)
number_sequence.reverse()
for sec_right in number_sequence[:finish]:
    if sec_right == '0':
        tot_seconds_right *= 0.8
    tot_seconds_right += int(sec_right)
if tot_seconds_right > tot_seconds_left:
    print(f'The winner is left with total time: {tot_seconds_left:.1f}')
else:
    print(f'The winner is right with total time: {tot_seconds_right:.1f}')
