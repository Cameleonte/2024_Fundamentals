list_of_integer_numbers = input().split()
numbers_to_remove = int(input())

list_of_integers = []
for digit in list_of_integer_numbers:
    list_of_integers.append(int(digit))
for value in range(numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))
print(*list_of_integers, sep=', ')
