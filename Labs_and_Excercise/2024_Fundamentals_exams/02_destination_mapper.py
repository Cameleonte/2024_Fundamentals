import re


def main(data):
    pattern = r'([=/])([A-Z][A-Za-z]{2,})\1'
    solution = re.finditer(pattern, data)
    travel_points = 0
    valid_destination = []

    for current_destination in solution:
        valid_destination.append(current_destination.group(2))
        current_points = len(current_destination.group(2))
        travel_points += current_points

    print_destinations = ', '.join(valid_destination)
    print(f'Destinations: {print_destinations}')
    print(f'Travel Points: {travel_points}')


string = input()
main(string)
