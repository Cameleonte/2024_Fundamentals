user_data = float(input())
number_is_in = False

while True:
    if 1 <= user_data <= 100:
        number_is_in = True
        break
    user_data = float(input())
print(f'The number {user_data} is between 1 and 100')
