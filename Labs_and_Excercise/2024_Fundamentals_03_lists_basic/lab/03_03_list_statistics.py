lines_number = int(input())
positives_list = []
negatives_list = []

for number in range(lines_number):
    user_input = int(input())
    if user_input >= 0:
        positives_list.append(user_input)
    else:
        negatives_list.append(user_input)

print(positives_list)
print(negatives_list)
print(f'Count of positives: {len(positives_list)} \nSum of negatives: {sum(negatives_list)}')
