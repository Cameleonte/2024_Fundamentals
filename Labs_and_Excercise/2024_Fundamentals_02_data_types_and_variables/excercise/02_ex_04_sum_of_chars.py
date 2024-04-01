lines_number = int(input())

total_sum = 0

for line in range(lines_number):
    letter = input()
    total_sum += ord(letter)
print(f'The sum equals: {total_sum}')
