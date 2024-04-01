def multiplication():
    tot_multiplication_sum = 0
    for char1 in range(0, len(first) + 1):
        if char1 < len(second):
            for char2 in range(char1, len(second) + 1):
                if char2 < len(first):
                    tot_multiplication_sum += ord(first[char1]) * ord(second[char2])
                    char1 += 1
                    break
    return tot_multiplication_sum


def addition(current_sum):
    if len(first) > len(second):
        for char in first[len(second):]:
            current_sum += ord(char)
    else:
        for char in second[len(first):]:
            current_sum += ord(char)
    return current_sum


string_input = input()
first, second = string_input.split()
tot_sum = 0

if first == second:
    tot_sum = multiplication()
else:
    tot_sum = multiplication() + addition(tot_sum)

print(tot_sum)
