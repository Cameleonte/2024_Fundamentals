first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students = int(input())

needed_hours = 1
reception_efficiency_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

if students // reception_efficiency_per_hour == 1 or students / reception_efficiency_per_hour < 1:
    print(f'Time needed: {needed_hours}h.')
else:
    for num in range(students // reception_efficiency_per_hour, students + 1):
        needed_hours += 1
        if students / reception_efficiency_per_hour < 1:
            print(f'Time needed: {needed_hours}h.')
