from math import sqrt
from math import floor


def coordinates(x1, y1, x2, y2):
    length_line_1 = sqrt(x1**2 + y1**2)
    length_line_2 = sqrt(x2**2 + y2**2)
    if length_line_1 > length_line_2:
        center_closer_point = floor(x2), floor(y2)
    else:
        center_closer_point = floor(x1), floor(y1)
    return center_closer_point


first_number = float(input())
second_number = float(input())
third_number = float(input())
forth_number = float(input())
print(coordinates(first_number, second_number, third_number, forth_number))
