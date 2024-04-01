from math import floor
from math import sqrt


def compare_lines_length(x1, y1, x2, y2, x3, y3, x4, y4):
    """Checking the signs of the coordinates and determinating their positions"""
    global line1_length, line2_length
    if (x1 >= 0 >= x2 or x1 <= 0 <= x2) and (y1 >= 0 >= y2 or y1 <= 0 <= y2):
        line1_length = sqrt((x1 ** 2 + x2 ** 2) + (y1 ** 2 + y2 ** 2))
    if x1 > 0 < x2 or x1 < 0 > x2:
        line1_length = sqrt(abs(x1 ** 2 - x2 ** 2) + (y1 ** 2 + y2 ** 2))
    if y1 > 0 < y2 or y1 < 0 > y2:
        line1_length = sqrt((x1 ** 2 + x2 ** 2) + abs(y1 ** 2 - y2 ** 2))
    if (x3 >= 0 >= x4 or x3 <= 0 <= x4) and (y3 >= 0 >= y4 or y3 <= 0 <= y4):
        line2_length = sqrt((x3 ** 2 + x4 ** 2) + (y3 ** 2 + y4 ** 2))
    if x3 > 0 < x4 or x3 < 0 > x4:
        line2_length = sqrt(abs(x3 ** 2 - x4 ** 2) + (y3 ** 2 + y4 ** 2))
    if y3 > 0 < y4 or y3 < 0 > y4:
        line2_length = sqrt((x3 ** 2 + x4 ** 2) + abs(y3 ** 2 - y4 ** 2))
    """Comparing the length of the lines"""
    if line1_length > line2_length:
        coordinates_result = (closer_point_to_center1(x1, y1, x2, y2))
    else:
        coordinates_result = (closer_point_to_center2(x3, y3, x4, y4))

    return coordinates_result


def left_coordinates(x1, y1, x2, y2, x3, y3, x4, y4):
    my_coordinates1 = [x1, y1, x2, y2]
    my_coordinates2 = [x3, y3, x4, y4]
    new_list1 = filter(closer_point_to_center1(x1, y1, x2, y2), my_coordinates1)
    if closer_point_to_center2(x3, y3, x4, y4) in my_list2:
        new_list2 = my_list2.remove(closer_point_to_center2(x3, y3, x4, y4))
    return new_list1, new_list2


def closer_point_to_center1(x1, y1, x2, y2):
    length_line_1 = sqrt(x1 ** 2 + y1 ** 2)
    length_line_2 = sqrt(x2 ** 2 + y2 ** 2)
    if length_line_1 > length_line_2:
        center_closer_point = floor(x2), floor(y2)
    else:
        center_closer_point = floor(x1), floor(y1)
    return center_closer_point


def closer_point_to_center2(x3, y3, x4, y4):
    length_line_1 = sqrt(x3 ** 2 + y3 ** 2)
    length_line_2 = sqrt(x3 ** 2 + y4 ** 2)
    if length_line_1 > length_line_2:
        center_closer_point = floor(x4), floor(y4)
    else:
        center_closer_point = floor(x3), floor(y3)
    return center_closer_point


line1_length = 0
line2_length = 0
new_list1 = []
new_list2 = []
first_number = float(input())
second_number = float(input())
third_number = float(input())
forth_number = float(input())
fifth_number = float(input())
sixth_number = float(input())
seventh_number = float(input())
eight_number = float(input())
print(compare_lines_length(first_number, second_number, third_number, forth_number,
                           fifth_number, sixth_number, seventh_number, eight_number), end='')
print(left_coordinates(first_number, second_number, third_number, forth_number,
                       fifth_number, sixth_number, seventh_number, eight_number))
