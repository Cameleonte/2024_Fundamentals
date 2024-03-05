from math import ceil
people_to_elevate = int(input())
elevator_capacity = int(input())
next_course = 0
first_courses = people_to_elevate // elevator_capacity
if people_to_elevate % elevator_capacity != 0:
    next_course = ceil((people_to_elevate % elevator_capacity) / elevator_capacity)
tot_courses = first_courses + next_course
print(tot_courses)

'''
from math import ceil
people = int(input())
capacity = int(input())
courses = ceil(people / capacity)
print(courses)
'''