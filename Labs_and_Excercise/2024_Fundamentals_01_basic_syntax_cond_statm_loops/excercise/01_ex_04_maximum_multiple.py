divisor = int(input())
boundary = int(input())
largest_integer = 0

if boundary % divisor == 0:
    largest_integer = boundary
else:
    for number in range(boundary - 1, divisor, - 1):
        if number % divisor == 0:
            largest_integer = number
            break

print(largest_integer)
