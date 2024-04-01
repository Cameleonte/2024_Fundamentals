symbol1 = input()
symbol2 = input()
random_string = input()

tot_sum = 0
first_value = ord(symbol1)
second_value = ord(symbol2)
given_range = range(first_value + 1, second_value)
for char in random_string:
    if ord(char) in given_range:
        tot_sum += ord(char)

print(tot_sum)
