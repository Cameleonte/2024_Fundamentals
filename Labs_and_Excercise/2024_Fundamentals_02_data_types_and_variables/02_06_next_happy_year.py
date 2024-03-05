'''year = int(input())

while True:
    year += 1
    distinct_number = True
    happy_year = ''
    for digit in str(year):
        if digit in happy_year:
            distinct_number = False
            break
        happy_year += digit
    if distinct_number:
        break
print(happy_year)
'''
year = int(input())

while True:
    year += 1
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        break
print(year)
