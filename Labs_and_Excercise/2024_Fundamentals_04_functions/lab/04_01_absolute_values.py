number_sequence = input().split()

absolute_values = []
for number in number_sequence:
    absolute_values.append(abs(float(number)))

print(absolute_values)
