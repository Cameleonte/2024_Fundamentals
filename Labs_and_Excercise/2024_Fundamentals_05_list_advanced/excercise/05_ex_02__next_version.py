input_version = list(map(int, input().split('.')))
input_version[-1] += 1
for num in range(len(input_version) - 1, 0, - 1):
    if input_version[num] > 9:
        input_version[num] = 0
        input_version[num - 1] += 1

print('.'.join(str(num) for num in input_version))
