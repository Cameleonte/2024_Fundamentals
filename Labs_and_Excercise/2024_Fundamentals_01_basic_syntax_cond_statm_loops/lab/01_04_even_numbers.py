n = int(input())

for number in range(1, n + 1):
    user_number = int(input())
    if user_number % 2 != 0:
        print(f'{user_number} is odd!')
        break
else:
    print("All numbers are even.")
