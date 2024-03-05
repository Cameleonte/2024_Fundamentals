first_string = input()
second_string = input()
last_string = first_string

for chars in range(1, len(first_string) + 1):
    first_part = second_string[:chars]
    second_part = first_string[chars:]
    new_string = first_part + second_part
    if new_string != last_string:
        print(new_string)
    last_string = new_string
